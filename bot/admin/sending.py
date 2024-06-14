from aiogram import types
from aiogram.types import ReplyKeyboardRemove
from bot.utils.constants import MAKE_SENDING_TEXT, CONFIRM_SENDING_TEXT, SUCCESS_SENDING
from bot.utils.keyboards import admin_sending_confirm_kb, admin_menu_kb

from aiogram.fsm.context import FSMContext
from bot.states.form import Admin

from bot.db import get_users


async def make_sending_command(message: types.Message, state: FSMContext):
    await message.answer(
        MAKE_SENDING_TEXT,
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(Admin.making_sending)


sender: str
message_id: int


async def get_message_command(message: types.Message, state: FSMContext):
    global sender, message_id
    await message.bot.copy_message(chat_id=message.chat.id, from_chat_id=message.chat.id, message_id=message.message_id)
    await message.answer(CONFIRM_SENDING_TEXT, reply_markup=admin_sending_confirm_kb)
    await state.set_state(Admin.confirm_sending)

    sender = message.chat.id
    message_id = message.message_id


async def process_sending_command(message: types.Message, state: FSMContext):
    count = 0
    for user in get_users():
        try:
            await message.bot.copy_message(chat_id=user, from_chat_id=sender, message_id=message_id)
            count += 1
        except Exception as e:
            print(e)
    await message.answer(SUCCESS_SENDING.format(count), reply_markup=admin_menu_kb)
    await state.set_state(Admin.menu)


