from aiogram import types
from aiogram.fsm.context import FSMContext

from bot.states.form import Form
from bot.utils.keyboards import get_skins_kb, main_menu_kb
from bot.utils.constants import GET_SKINS_TEXT, BAD_LINK_REQUEST, BAD_BALANCE_REQUEST, GOOD_REQUEST
from bot.db import get_show_info, create_ticket


async def get_skins_command(message: types.Message, state: FSMContext):
    await message.answer(
        GET_SKINS_TEXT.format(*get_show_info(message.from_user.id)[:-1]),
        reply_markup=get_skins_kb, disable_web_page_preview=True)
    await state.set_state(Form.get_skins)


async def confirm_command(message: types.Message, state: FSMContext):
    link, balance = get_show_info(message.from_user.id)[:-1]
    if link == '-':
        await message.answer(
            BAD_LINK_REQUEST, reply_markup=get_skins_kb
        )
    elif balance == 0:
        await message.answer(
            BAD_BALANCE_REQUEST, reply_markup=get_skins_kb
        )
    else:
        create_ticket(message.from_user.id, message.from_user.username)
        await message.answer(
            GOOD_REQUEST, reply_markup=main_menu_kb
        )
    await state.clear()
