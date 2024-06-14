import sys
from os import getenv
import asyncio
import logging

import motor
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from bot.handlers.commands import register_handlers
from bot.admin.commands import register_admin_handlers


TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher(storage=MemoryStorage())

register_admin_handlers(dp)
register_handlers(dp)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
