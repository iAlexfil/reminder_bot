from aiogram import types
from bot.utils.keyboards import main_menu_kb
from bot.utils.constants import INVITE_FRIENDS_TEXT


async def invite_friend_command(message: types.Message):
    await message.answer(
        INVITE_FRIENDS_TEXT.format(message.from_user.id),
        reply_markup=main_menu_kb, disable_web_page_preview=True)
