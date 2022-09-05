import asyncio

from aiogram import *
from py_linq import Enumerable
from misc import bot, dp
from aiogram.types import ChatType, ChatMemberStatus, Message
from text import get_text_args
from ext import ExtendedMessage
from commands import get_allowed_commands, ExtendedBotCommand


def get_extended_command(name: str) -> ExtendedBotCommand:
    return Enumerable(get_allowed_commands()).first(lambda com: com.name == name)


def is_allowed_chat(command: ExtendedBotCommand, chat_type: ChatType) -> bool:
    return True if command.allowed_chat_types is None else chat_type in command.allowed_chat_types


def is_owner(status: ChatMemberStatus) -> bool:
    return status == ChatMemberStatus.OWNER or status == ChatMemberStatus.CREATOR


def is_administrator(status: ChatMemberStatus) -> bool:
    return status == ChatMemberStatus.ADMINISTRATOR or is_owner(status)


def has_required_status(command: ExtendedBotCommand, status: ChatMemberStatus) -> bool:
    if len(command.required_statuses) == 0:
        return is_owner(status)
    return status in command.required_statuses or is_owner(status)


def can_execute(command: ExtendedBotCommand, chat_type: ChatType, status: ChatMemberStatus) -> bool:
    return is_allowed_chat(command, chat_type) and has_required_status(command, status)


async def check_ability_to_execute(command: ExtendedBotCommand, message: Message) -> bool:
    member = await bot.get_chat_member(message.chat.id, message.from_user.id)

    return can_execute(command, message.chat.type, member.status)


@dp.message_handler(commands=["start"])
async def handle_start(message: ExtendedMessage):
    this_command = get_extended_command("start")

    if not await check_ability_to_execute(this_command, message):
        await message.reply("Данная команда не может быть использована!")
        return

    await message.reply("Работа начата!")
    await bot.delete_my_commands()

    allowed_commands = Enumerable(get_allowed_commands())

    member_commands = allowed_commands \
        .where(lambda com: ChatMemberStatus.MEMBER in com.required_statuses) \
        .select(lambda com: com.bot_command) \
        .to_list()

    def filter_predicate(com: ExtendedBotCommand) -> bool:
        return ChatMemberStatus.ADMINISTRATOR in com.required_statuses \
               or ChatMemberStatus.CREATOR in com.required_statuses \
               or ChatMemberStatus.OWNER in com.required_statuses

    administrator_commands = allowed_commands \
        .where(filter_predicate) \
        .select(lambda com: com.bot_command) \
        .to_list()

    await bot.set_my_commands(member_commands, types.BotCommandScopeAllGroupChats())
    await bot.set_my_commands(administrator_commands, types.BotCommandScopeAllChatAdministrators())


@dp.message_handler(commands=["help"])
async def handle_help(message: ExtendedMessage) -> None:
    allowed_commands = Enumerable(get_allowed_commands())
    this_command = allowed_commands.first(lambda com: com.name == "help")

    if not await check_ability_to_execute(this_command, message):
        await message.reply("Данная команда не может быть использована!")
        return

    args = get_text_args(message.get_args())

    if args:
        if len(args) != 1:
            await message.reply("Команда поддерживает только 1 аргумент!")
            return

        arg = args[0]

        if allowed_commands.any(lambda x: x.bot_command.command == arg):
            target = allowed_commands.first(lambda x: x.name == arg)
            await message.reply(f"/{target.bot_command.command} &#8212 {target.extended_description}\n"
                                f"Доступна для: {target.required_statuses}")
        else:
            await message.reply(f"Команда /{arg} не поддерживается!\n"
                                f"Для получения списка поддерживаемых команд используйте /help")

    else:
        supported_commands_text = "Поддерживаемые команды:\n"

        member = await bot.get_chat_member(message.chat.id, message.from_user.id)
        supported_commands = allowed_commands \
            .where(lambda com: can_execute(this_command, message.chat.type, member.status))

        for command in supported_commands:
            supported_commands_text += f"/{command.name}\n"

        await message.reply(supported_commands_text)


@dp.message_handler(commands=["send_after"])
async def handle_send_after(message: ExtendedMessage):
    this_command = get_extended_command("send_after")

    if not await check_ability_to_execute(this_command, message):
        await message.reply("Данная команда не может быть использована!")
        return

    args = get_text_args(message.get_args())

    if len(args) != 2:
        await message.reply("Команда требует два обязательных аргумента сообщение и количество времени в секундах!")
        return

    try:
        delay = int(args[1])
    except ValueError:
        await message.reply("Время задано в некорректном формате!")
        return

    await asyncio.sleep(delay)
    await message.answer(args[0])
