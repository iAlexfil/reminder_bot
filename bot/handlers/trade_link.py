from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

import bot.db
from bot.states.form import Form

from bot.utils.check_url import is_valid_url
from bot.utils.keyboards import lk_kb

from bot.utils.constants import ASK_FOR_TRADE_LINK, SUCCESS_TRADE_LINK, INVALID_TRADE_LINK


async def change_trade_link(message: types.Message, state: FSMContext):
    await message.answer(ASK_FOR_TRADE_LINK, reply_markup=ReplyKeyboardRemove())
    await state.set_state(Form.trade_link)


async def set_trade_link(message: types.Message, state: FSMContext):
    if is_valid_url(message.text):
        bot.db.change_trade_link(message.from_user.id, message.text)
        await message.answer(SUCCESS_TRADE_LINK, reply_markup=lk_kb)
    else:
        await message.answer(INVALID_TRADE_LINK, reply_markup=lk_kb)
    await state.clear()
