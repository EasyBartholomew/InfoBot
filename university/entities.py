from datetime import date, time
from strext import is_none_or_whitespace


def verify_optional_str(value: str) -> str:
    return value if not is_none_or_whitespace(value) else "не задано"


class StudyingStageEntity:

    def __init__(self, name: str, letter: str):
        self.__name = name
        self.__letter = letter

    @property
    def name(self) -> str:
        return self.__name

    @property
    def letter(self) -> str:
        return self.__letter


class Institute:

    def __init__(self, name: str, letter: str, short_name: str = None):
        self.__name = name
        self.__letter = letter
        self.__short_name = verify_optional_str(short_name)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def letter(self) -> str:
        return self.__letter

    @property
    def short_name(self) -> str:
        return self.__short_name

    def __str__(self):
        return self.name


class ResolvedGroup:

    def __init__(self, name: str, institute: Institute, stage: StudyingStageEntity, course: int, number: str):
        self.__name = name
        self.__institute = institute
        self.__stage = stage
        self.__course = course
        self.__number = number

    @property
    def name(self) -> str:
        return self.__name

    @property
    def institute(self) -> Institute:
        return self.__institute

    @property
    def stage(self) -> StudyingStageEntity:
        return self.__stage

    @property
    def course(self) -> int:
        return self.__course

    @property
    def number(self) -> str:
        return self.__number

    def __str__(self):
        return f"Name=\"{self.name}\"; Institute=\"{self.institute}\"; " \
               f"Stage={self.stage.name}; Course={self.course}; Number={self.number}"


class TimeUnitEntity:
    def __init__(self, index: int, begin: time, end: time):
        self.__index = index
        self.__begin = begin
        self.__end = end

    @property
    def index(self) -> int:
        return self.__index

    @property
    def begin(self) -> time:
        return self.__begin

    @property
    def end(self) -> time:
        return self.__end


class AttestationTypeEntity:
    def __init__(self, name: str, short_name: str = None):
        self.__name = name
        self.__short_name = verify_optional_str(short_name)

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name


class Subject:
    def __init__(self, name: str, short_name: str = None, attestation_type: AttestationTypeEntity = None):
        self.__name = name
        self.short_name = short_name
        self.attestation_type = attestation_type

    @property
    def name(self) -> str:
        return self.__name

    @property
    def short_name(self) -> str:
        return self.__short_name

    @short_name.setter
    def short_name(self, value: str):
        self.__short_name = verify_optional_str(value)

    @property
    def attestation_type(self) -> AttestationTypeEntity:
        return self.__attestation_type

    @attestation_type.setter
    def attestation_type(self, value: AttestationTypeEntity):
        self.__attestation_type = value


class Lesson:
    def __init__(self, when: date,
                 unit: TimeUnitEntity,
                 subject: Subject,
                 lesson_type: str = None,
                 classroom: str = None,
                 professor: str = None):
        self.__date = when
        self.__unit = unit
        self.__subject = subject
        self.type = lesson_type
        self.classroom = classroom
        self.professor = professor

    @property
    def date(self) -> date:
        return self.__date

    @property
    def unit(self) -> TimeUnitEntity:
        return self.__unit

    @property
    def subject(self) -> Subject:
        return self.__subject

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, value: str):
        self.__type = verify_optional_str(value)

    @property
    def classroom(self) -> str:
        return self.__classroom

    @classroom.setter
    def classroom(self, value: str):
        self.__classroom = verify_optional_str(value)

    @property
    def professor(self) -> str:
        return self.__professor

    @professor.setter
    def professor(self, value: str):
        self.__professor = verify_optional_str(value)
