from aiogram import types
from bot.utils.keyboards import admin_menu_kb
from bot.utils.constants import HELLO_ADMIN_TEXT

from aiogram.fsm.context import FSMContext
from bot.states.form import Admin


admin_ids = [960437557, 5023398458]


async def enter_command(message: types.Message, state: FSMContext):
    if message.from_user.id not in admin_ids:
        return
    await message.answer(
        HELLO_ADMIN_TEXT,
        reply_markup=admin_menu_kb
    )
    await state.set_state(Admin.menu)

