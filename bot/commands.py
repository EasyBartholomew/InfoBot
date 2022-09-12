from aiogram.types import BotCommand, ChatType, ChatMemberStatus
from py_linq import Enumerable
from typing import List

DEFAULT_ALLOWED_CHAT_TYPES = [ChatType.GROUP, ChatType.SUPERGROUP]
DEFAULT_REQUIRED_STATUSES = [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR]


class ExtendedBotCommand:

    def __init__(self, name: str, description: str, extended_description: str, allowed_chat_types: list = None,
                 required_statuses: list = None):
        self.__bot_command = BotCommand(name, description)
        self.__extended_description = extended_description
        self.__allowed_chat_types = DEFAULT_ALLOWED_CHAT_TYPES if allowed_chat_types is None else allowed_chat_types
        self.__required_statuses = required_statuses \
            if required_statuses is not None \
            else DEFAULT_REQUIRED_STATUSES

    @property
    def bot_command(self) -> BotCommand:
        return self.__bot_command

    @property
    def extended_description(self) -> str:
        return self.__extended_description

    @property
    def name(self) -> str:
        return self.bot_command.command

    @property
    def description(self) -> str:
        return self.bot_command.description

    @property
    def allowed_chat_types(self) -> List[ChatType]:
        return self.__allowed_chat_types

    @property
    def required_statuses(self) -> List[ChatMemberStatus]:
        return self.__required_statuses


ALLOWED_COMMANDS = [
    ExtendedBotCommand("help", "получение информации о командах",
                       "используйте данную команду для получения сведений о существующих командах\n"
                       "syntax: /help or /help command_name"),

    ExtendedBotCommand("start", "запуск бота", "используйте данную команду для запуска бота",
                       required_statuses=[ChatMemberStatus.ADMINISTRATOR]),

    ExtendedBotCommand("send_after", "отправка сообщения через заданное время",
                       "используйте данную команду, чтобы отправить сообщение через некоторое количество секунд\n"
                       "syntax: /send_after позвонить Иванову, 30 or /send_after \"\"Белый, чёрный\"\", 30"),

    ExtendedBotCommand("get", "получение расписания",
                       "используйте данную команду для получения расписания в указанную дату.\n"
                       "syntax:\n"
                       "/get\n"
                       "/get 12.02;\n"
                       "/get 12.02.2022;\n"
                       "/get 12.02.22\n")
]


def get_allowed_commands() -> List[ExtendedBotCommand]:
    return ALLOWED_COMMANDS


def get_extended_command(name: str) -> ExtendedBotCommand:
    return Enumerable(get_allowed_commands()).first(lambda com: com.name == name)
