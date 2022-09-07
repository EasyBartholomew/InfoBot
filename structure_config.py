from structure import Institute, StudyingStageEntity
from enum import Enum

INSTITUTES = [

    Institute("Кибербезопасности и цифровых технологий", "Б", "КБ"),
    Institute("Информационных технологий", "И", "ИТ"),
    Institute("Не поддерживается", "", "НП")
    # TODO: Add others here
]


class StudyingStage(Enum):
    BACHELOR = StudyingStageEntity("Бакалавриат", "Б")
    MASTER = StudyingStageEntity("Магистратура", "М")
    SPECIALIST = StudyingStageEntity("Специалитет", "С")
    UNKNOWN = StudyingStageEntity("Неизвестно", "Н")


def get_institutes() -> list:
    return INSTITUTES


def get_studying_stages() -> list:
    return [stage.value for stage in StudyingStage]
