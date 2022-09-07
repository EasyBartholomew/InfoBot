import typing
from aiogram.types import Message, InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply, \
    MessageEntity, base


class ExtendedMessage(Message):
    async def reply(
            self,
            text: base.String,
            parse_mode: typing.Optional[base.String] = None,
            entities: typing.Optional[typing.List[MessageEntity]] = None,
            disable_web_page_preview: typing.Optional[base.Boolean] = None,
            disable_notification: typing.Optional[base.Boolean] = True,
            protect_content: typing.Optional[base.Boolean] = None,
            allow_sending_without_reply: typing.Optional[base.Boolean] = None,
            reply_markup: typing.Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
                None,
            ] = None,
            reply: base.Boolean = True,
    ) -> Message:
        return await super().reply(text, parse_mode, entities, disable_web_page_preview, disable_notification,
                                   protect_content, allow_sending_without_reply, reply_markup, reply)

    async def answer(
            self,
            text: base.String,
            parse_mode: typing.Optional[base.String] = None,
            entities: typing.Optional[typing.List[MessageEntity]] = None,
            disable_web_page_preview: typing.Optional[base.Boolean] = None,
            disable_notification: typing.Optional[base.Boolean] = True,
            protect_content: typing.Optional[base.Boolean] = None,
            allow_sending_without_reply: typing.Optional[base.Boolean] = None,
            reply_markup: typing.Union[
                InlineKeyboardMarkup,
                ReplyKeyboardMarkup,
                ReplyKeyboardRemove,
                ForceReply,
                None,
            ] = None,
            reply: base.Boolean = False,
    ) -> Message:
        return await super().answer(text, parse_mode, entities, disable_web_page_preview, disable_notification,
                                    protect_content, allow_sending_without_reply, reply_markup, reply)
