from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.states.form import Form
from bot.utils.keyboards import lk_kb
from bot.utils.constants import LK_TEXT
from bot.db import get_show_info


async def lk_command(message: types.Message, state: FSMContext):
    await message.answer(
        LK_TEXT.format(*get_show_info(message.from_user.id)),
        reply_markup=lk_kb, disable_web_page_preview=True)
    await state.set_state(Form.lk)
