from university.entities import *
from structure import get_institutes, get_studying_stages
from bot.text import is_none_or_whitespace
from py_linq import Enumerable
from datetime import date
import re


class WrongPatternError(Exception):
    pass


def calculate_course(admission_year: int) -> int:
    now = date.today()
    return now.year - admission_year + (0 if now.month < 8 else 1)


def resolve_group(group_name: str) -> ResolvedGroup:
    if is_none_or_whitespace(group_name):
        raise ValueError("group_name can not be None, empty or whitespace string!")

    group_name = group_name.strip().upper()
    match = re.match(r"[А-Я]{2}[МБ][ОЗ]-\d{2}-\d{2}", group_name)

    if not match:
        raise WrongPatternError("regex is not satisfied!")

    institutes = Enumerable(get_institutes())
    stages = Enumerable(get_studying_stages())

    # First letter indicates institute
    institute_letter = group_name[0]

    # Third letter indicates grade
    stage_letter = group_name[2]

    # The first two digits indicate number
    number = group_name[5] + group_name[6]

    # The second two digits indicate year of getting through
    year_str = group_name[8] + group_name[9]

    if institutes.all(lambda inst: inst.letter != institute_letter):
        institute_letter = ""

    if stages.all(lambda stg: stg.letter != stage_letter):
        stage_letter = ""

    institute = institutes.first(lambda inst: inst.letter == institute_letter)
    stage = stages.first(lambda stg: stg.letter == stage_letter)
    course = calculate_course(2000 + int(year_str))

    return ResolvedGroup(group_name, institute, stage, course, number)
