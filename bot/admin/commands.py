from aiogram import Dispatcher

from aiogram.filters import Command

from bot.states.form import Admin

from bot.utils.TextFilter import TextFilter, LowerTextFilter
from bot.utils.constants import *

from bot.admin.enter import enter_command
from bot.handlers.back import back_command
from bot.admin.sending import get_message_command, make_sending_command, process_sending_command
from bot.admin.tickets import tickets_command, next_command, confirm_request, reject_request


def register_admin_handlers(dp: Dispatcher):
    dp.message.register(enter_command, LowerTextFilter(KEYWORD))
    dp.message.register(enter_command, TextFilter(BACK_BUTTON), Admin.confirm_sending)
    dp.message.register(back_command, TextFilter(EXIT_ADMIN_MODE_BUTTON))

    dp.message.register(make_sending_command, TextFilter(MAKE_SENDING_BUTTON), Admin.menu)
    dp.message.register(get_message_command, Admin.making_sending)
    dp.message.register(process_sending_command, Admin.confirm_sending, TextFilter(AGREE_SENDING_BUTTON))

    dp.message.register(make_sending_command, TextFilter(CHANGE_MESSAGE_BUTTON), Admin.confirm_sending)

    dp.message.register(tickets_command, Admin.menu, TextFilter(TICKETS_BUTTON))
    dp.message.register(next_command, Admin.tickets, TextFilter(SHOW_TICKETS_BUTTON))
    dp.message.register(confirm_request, Admin.showing_tickets, TextFilter(MARK_COMPLETE_BUTTON))
    dp.message.register(reject_request, Admin.showing_tickets, TextFilter(REJECT_BUTTON))

    dp.message.register(enter_command, Admin.showing_tickets, TextFilter(BACK_BUTTON))
    dp.message.register(enter_command, Admin.tickets, TextFilter(BACK_BUTTON))
