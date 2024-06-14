from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.utils.keyboards import main_menu_kb

from bot.db import add_user, exist_user, increase_balance
from bot.states.form import Form


def process_ref(ref_code: str):
    try:
        ref_code = int(ref_code)
    except ValueError:
        return

    if exist_user(ref_code):
        increase_balance(ref_code)


async def start_command(message: types.Message, state: FSMContext):
    if not exist_user(message.from_user.id):
        add_user(message.from_user.id)
        args = message.text.split()
        if len(args) > 1:
            process_ref(args[1])

    await message.answer("Hello мир", reply_markup=main_menu_kb)
    await state.clear()
