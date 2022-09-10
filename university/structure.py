from university.entities import Institute, StudyingStageEntity, TimeUnitEntity, AttestationTypeEntity
from enum import Enum
from datetime import time
from py_linq import Enumerable

INSTITUTES = [

    Institute("Институт кибербезопасности и цифровых технологий", "Б", "ИКБ"),
    Institute("Институт информационных технологий", "И", "ИИТ"),
    Institute("Институт искусственного интеллекта", "К", "ИИИ"),
    Institute("Институт перспективных технологий и индустриального программирования", "Э", "ИПТИП"),
    Institute("Институт перспективных технологий и индустриального программирования", "Т", "ИПТИП"),
    Institute("Институт радиоэлектроники и информатики", "Р", "ИРИ"),
    Institute("Институт технологий управления", "У", "ИТУ"),
    Institute("Институт тонких химических технологий им. М.В. Ломоносова", "Х", "ИТХТ"),
    Institute("не поддерживается", "")

]


class StudyingStage(Enum):
    BACHELOR = StudyingStageEntity("Бакалавриат", "Б")
    SPECIALIST = StudyingStageEntity("Специалитет", "С")
    MASTER = StudyingStageEntity("Магистратура", "М")
    UNKNOWN = StudyingStageEntity("Неизвестно", "")


def get_institutes() -> list:
    return INSTITUTES


def get_studying_stages() -> list:
    return [stage.value for stage in StudyingStage]


class TimeUnit(Enum):
    FIRST = TimeUnitEntity(1, time(9), time(10, 30))
    SECOND = TimeUnitEntity(2, time(10, 40), time(12, 10))
    THIRD = TimeUnitEntity(3, time(12, 40), time(14, 10))
    FOURTH = TimeUnitEntity(4, time(14, 20), time(15, 50))
    FIFTH = TimeUnitEntity(5, time(16, 20), time(17, 50))
    SIXTH = TimeUnitEntity(6, time(18), time(19, 30))
    SEVENTH = TimeUnitEntity(7, time(19, 40), time(21, 10))


def get_unit_by_index(index: int) -> TimeUnitEntity | None:
    return Enumerable([unit.value for unit in TimeUnit]).first_or_default(lambda unit: unit.index == index)


class AttestationType(Enum):
    OFFSET = AttestationTypeEntity("Зачёт", "З")
    COURSE_WORK = AttestationTypeEntity("Курсовая работа", "К")
    EXAM = AttestationTypeEntity("Экзамен", "Э")
