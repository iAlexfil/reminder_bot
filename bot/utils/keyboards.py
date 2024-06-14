from aiogram import types
from bot.utils.constants import *


main_menu_kb = types.ReplyKeyboardMarkup(keyboard=[
    [
        types.KeyboardButton(text=LK_BUTTON),
        types.KeyboardButton(text=CONTACTS_BUTTON)
    ],
    [
        types.KeyboardButton(text=GET_SKINS_BUTTON),
        types.KeyboardButton(text=INVITE_BUTTON)
    ],
], resize_keyboard=True)


lk_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text=TRADE_LINK_BUTTON)],
    [types.KeyboardButton(text=BACK_BUTTON)]
], resize_keyboard=True)

get_skins_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text=AGREE_BUTTON)],
    [types.KeyboardButton(text=BACK_BUTTON)]
], resize_keyboard=True)


admin_menu_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text=MAKE_SENDING_BUTTON)],
    [types.KeyboardButton(text=TICKETS_BUTTON)],
    [types.KeyboardButton(text=EXIT_ADMIN_MODE_BUTTON)]
], resize_keyboard=True)

admin_sending_confirm_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text=AGREE_SENDING_BUTTON)],
    [types.KeyboardButton(text=CHANGE_MESSAGE_BUTTON)],
    [types.KeyboardButton(text=BACK_BUTTON)]
], resize_keyboard=True)

admin_tickets_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text=SHOW_TICKETS_BUTTON)],
    [types.KeyboardButton(text=BACK_BUTTON)]
], resize_keyboard=True)


admin_showing_tickets_kb = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text=MARK_COMPLETE_BUTTON)],
    [types.KeyboardButton(text=REJECT_BUTTON)],
    [types.KeyboardButton(text=BACK_BUTTON)]
], resize_keyboard=True)
