import asyncio
import logging
import config
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

from bot.controller import *


def setup():
    executor.start_polling(dp, loop=loop, skip_updates=True)
