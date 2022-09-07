from university.entities import Institute, StudyingStageEntity
from enum import Enum

INSTITUTES = [

    Institute("кибербезопасности и цифровых технологий", "Б", "КБ"),
    Institute("информационных технологий", "И", "ИТ"),
    Institute("искусственного интеллекта", "К", "ИИ"),
    Institute("перспективных технологий и индустриального программирования (Вернадского 78)", "Э", "ПТИП"),
    Institute("перспективных технологий и индустриального программирования (Стромынка 20)", "Т", "ПТИП"),
    Institute("радиоэлектроники и информатики", "Р", "РИ"),
    Institute("технологий управления", "У", "ТУ"),
    Institute("тонких химических технологий им. М.В. Ломоносова", "Х", "ТХТ"),
    Institute("не поддерживается", "", "НП")

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
