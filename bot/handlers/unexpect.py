from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.utils.constants import UNEXPECT_TEXT


async def unexpext_command(message: types.Message, state: FSMContext):
    await message.answer(UNEXPECT_TEXT)
