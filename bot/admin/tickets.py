from aiogram import types

from aiogram.fsm.context import FSMContext
from bot.states.form import Admin

from bot.utils.constants import HELLO_TICKETS_TEXT, SHOWING_TICKETS_TEXT, PROCESSED_REQUEST_TEXT, YOUR_REQUEST_REJECTED, YOUR_REQUEST_COMPLETED
from bot.utils.keyboards import admin_tickets_kb, admin_showing_tickets_kb
from bot.db import get_all_tickets, get_one_ticket, delete_ticket, reject_ticket


async def tickets_command(message: types.Message, state: FSMContext):
    data = get_all_tickets()
    await message.answer(HELLO_TICKETS_TEXT.format(len(data)), reply_markup=admin_tickets_kb)
    await state.set_state(Admin.tickets)


async def next_command(message: types.Message, state: FSMContext):
    ticket = get_one_ticket()
    if ticket is None:
        await message.answer("Нет неотвеченных запросов", reply_markup=admin_tickets_kb)
        await state.set_state(Admin.tickets)
        return

    await state.update_data(ticket=ticket)

    await message.answer(SHOWING_TICKETS_TEXT.format(ticket[0], ticket[3], ticket[5], ticket[2]),
                         reply_markup=admin_showing_tickets_kb)
    await state.set_state(Admin.showing_tickets)


async def confirm_request(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ticket = data['ticket']
    delete_ticket(ticket[0])

    await message.answer(PROCESSED_REQUEST_TEXT)
    try:
        await message.bot.send_message(ticket[1], text=YOUR_REQUEST_COMPLETED)
    except Exception as e:
        pass

    await next_command(message, state)


async def reject_request(message: types.Message, state: FSMContext):
    data = await state.get_data()
    ticket = data['ticket']
    reject_ticket(ticket[0])

    await message.answer(PROCESSED_REQUEST_TEXT)
    try:
        await message.bot.send_message(ticket[1], text=YOUR_REQUEST_REJECTED)
    except Exception as e:
        pass

    await next_command(message, state)
