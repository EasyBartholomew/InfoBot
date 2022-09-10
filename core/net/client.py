from requests import get
from requests.exceptions import ConnectionError
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from bs4.element import Tag
from py_linq import Enumerable
from enum import Enum
import core.net.config as config
import re


def download_target_page() -> str:
    url = urljoin(config.BASE_URL, config.SCHEDULE_ROUTE)

    response = get(url)

    if not response.ok:
        raise ConnectionError()

    return response.text


class CourseEntry:
    def __init__(self, course_name: str, links: list = None):
        self.__number = int(re.search(r"^\d", course_name.strip()).group(0))
        self.__links = links if links is not None else []

    @property
    def number(self) -> int:
        return self.__number

    @property
    def links(self) -> list:
        return self.__links


class Stage(Enum):
    GENERAL = 0
    MAGISTRACY = 1


class InstituteEntry:

    def __init__(self, institute_name: str, course_entries: list = None):
        self.__name = institute_name
        self.__course_entries = course_entries if course_entries is not None else []

    @property
    def name(self):
        return self.__name

    @property
    def course_entries(self):
        return self.__course_entries

    def __str__(self):
        return f"{self.name}:{len(self.course_entries)}"


class ScheduleParser:

    def __init__(self, html: str):
        self.__html = html
        self.__institutes_entries = None

    @property
    def institutes_entries(self) -> dict:
        if self.__institutes_entries is None:
            self.__institutes_entries = ScheduleParser.__parse_schedule(self.__html)

        return self.__institutes_entries

    @staticmethod
    def __parse_institute(a: Tag) -> InstituteEntry:
        name = a.text
        parent = a.parent.parent
        course_entries = {}

        courses = Enumerable(parent.find_all("div", {"class": "uk-width-1-2"})) \
            .select(lambda t: t.find("a", href=True))

        for course in courses:
            course_name = course.find("div").find("div").text.strip()

            if course_name not in course_entries.keys():
                course_entries[course_name] = CourseEntry(course_name)

            course_entries[course_name].links.append(course["href"])

        return InstituteEntry(name, list(course_entries.values()))

    @staticmethod
    def __parse_list(li: Tag) -> list:
        institutes = li.find_all("a", {"class": "uk-text-bold"})
        institute_entries = []

        for institute in institutes:
            result = ScheduleParser.__parse_institute(institute)
            institute_entries.append(result)

        return institute_entries

    @staticmethod
    def __parse_schedule(html: str) -> dict:
        soup = BeautifulSoup(html, features="html.parser")

        tabs = soup.find("ul", {"id": "tab-content"})
        lists = tabs.find_all("li")

        stages = {Stage.GENERAL: ScheduleParser.__parse_list(lists[0]),
                  Stage.MAGISTRACY: ScheduleParser.__parse_list(lists[1])}

        return stages
