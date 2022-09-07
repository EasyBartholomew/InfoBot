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

    def __init__(self, name: str, letter: str, short_name: str = "не задано"):
        self.__name = name
        self.__letter = letter
        self.__short_name = short_name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def letter(self) -> str:
        return self.__letter

    @property
    def short_name(self):
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
    def name(self):
        return self.__name

    @property
    def institute(self):
        return self.__institute

    @property
    def stage(self):
        return self.__stage

    @property
    def course(self):
        return self.__course

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f"Name=\"{self.name}\"; Institute=\"{self.institute}\"; " \
               f"Stage={self.stage.name}; Course={self.course}; Number={self.number}"
