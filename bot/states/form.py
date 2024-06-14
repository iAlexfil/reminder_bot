from aiogram.fsm.state import StatesGroup, State


class Form(StatesGroup):
    lk = State()

    trade_link = State()
    get_skins = State()


class Admin(StatesGroup):
    menu = State()
    making_sending = State()
    confirm_sending = State()
    tickets = State()
    showing_tickets = State()
