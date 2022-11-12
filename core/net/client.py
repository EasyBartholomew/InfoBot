from requests import get, Response
from requests.exceptions import ConnectionError
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from bs4.element import Tag
from enum import Enum
from typing import List, Dict
import core.net.config as config
import re


def get_page(url: str) -> Response:
    response = get(url)

    if not response.ok:
        raise ConnectionError()

    return response


def get_target_page() -> str:
    url = urljoin(config.BASE_URL, config.SCHEDULE_ROUTE)

    return get_page(url).text


class CourseEntry:
    def __init__(self, course_name: str, links: list = None):
        self.__number = int(re.search(r"^\d", course_name.strip()).group(0))
        self.__links = links if links is not None else []

    @property
    def number(self) -> int:
        return self.__number

    @property
    def links(self) -> List[str]:
        return self.__links


class Stage(Enum):
    GENERAL = 0
    MAGISTRACY = 1


class InstituteEntry:

    def __init__(self, institute_name: str, course_entries: list = None):
        self.__name = institute_name
        self.__courses = course_entries if course_entries is not None else []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def courses(self) -> List[CourseEntry]:
        return self.__courses

    def __str__(self):
        return f"{self.name}:{len(self.courses)}"


class ScheduleParser:

    def __init__(self, html: str):
        self.__html = html
        self.__schedule = None

    @property
    def schedule(self) -> Dict[Stage, List[InstituteEntry]]:
        if self.__schedule is None:
            self.__schedule = ScheduleParser.__parse_schedule(self.__html)

        return self.__schedule

    @staticmethod
    def __parse_institute(a: Tag) -> InstituteEntry:
        name = a.text
        parent = a.parent.parent
        course_entries = {}

        courses = [t.find("a", href=True) for t in parent.find_all("div", {"class": "uk-width-1-2"})]

        for course in courses:
            course_name = course.find("div").find("div").text.strip()

            if course_name not in course_entries.keys():
                course_entries[course_name] = CourseEntry(course_name)

            course_entries[course_name].links.append(course["href"])

        return InstituteEntry(name, list(course_entries.values()))

    @staticmethod
    def __parse_list(li: Tag) -> List[InstituteEntry]:
        institutes = li.find_all("a", {"class": "uk-text-bold"})
        institute_entries = []

        for institute in institutes:
            result = ScheduleParser.__parse_institute(institute)
            institute_entries.append(result)

        return institute_entries

    @staticmethod
    def __parse_schedule(html: str) -> Dict[Stage, List[InstituteEntry]]:
        soup = BeautifulSoup(html, features="html.parser")

        tabs = soup.find("ul", {"id": "tab-content"})
        lists = tabs.find_all("li")

        stages = {Stage.GENERAL: list(filter(lambda inst: inst.courses, ScheduleParser.__parse_list(lists[0]))),
                  Stage.MAGISTRACY: list(filter(lambda inst: inst.courses, ScheduleParser.__parse_list(lists[1])))}

        return stages
