from aiogram.types import BotCommand, ChatType, ChatMemberStatus

DEFAULT_ALLOWED_CHAT_TYPES = [ChatType.GROUP, ChatType.SUPERGROUP]
DEFAULT_REQUIRED_STATUSES = [ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR]


class ExtendedBotCommand:

    def __init__(self, bot_command: BotCommand, extended_description: str, allowed_chat_types: list = None,
                 required_statuses: list = None):
        self.__bot_command = bot_command
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
    def allowed_chat_types(self) -> list:
        return self.__allowed_chat_types

    @property
    def required_statuses(self):
        return self.__required_statuses


ALLOWED_COMMANDS = [
    ExtendedBotCommand(BotCommand("help", "получение информации о командах"),
                       "используйте данную команду для получения сведений о существующих командах\n"
                       "syntax: /help or /help command_name"),
    ExtendedBotCommand(BotCommand("start", "запуск бота"), "используйте данную команду для запуска бота",
                       required_statuses=[ChatMemberStatus.ADMINISTRATOR])
]


def get_allowed_commands() -> list:
    return ALLOWED_COMMANDS
