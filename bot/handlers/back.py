from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.utils.keyboards import main_menu_kb


async def back_command(message: types.Message, state: FSMContext):
    await message.answer("Вы в главном меню", reply_markup=main_menu_kb)
    await state.clear()
