from aiogram import Bot, Dispatcher, executor, types
import logging
import asyncio
import config

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN, parse_mode=types.ParseMode.HTML)
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)


def setup():
    import controller
    executor.start_polling(dp, loop=loop, skip_updates=True)
