from aiogram import types
from bot.utils.keyboards import main_menu_kb
from bot.utils.constants import CONTACTS_TEXT


async def contacts_command(message: types.Message):
    await message.answer(
        CONTACTS_TEXT,
        reply_markup=main_menu_kb, disable_web_page_preview=True)
