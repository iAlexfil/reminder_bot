from aiogram import Dispatcher

from bot.handlers.contacts import contacts_command
from bot.handlers.start import start_command
from bot.handlers.lk import lk_command
from bot.handlers.back import back_command
from bot.handlers.trade_link import change_trade_link, set_trade_link
from bot.handlers.get_skins import get_skins_command, confirm_command
from bot.handlers.invite_friend import invite_friend_command

from aiogram.filters import Command

from bot.handlers.unexpect import unexpext_command
from bot.utils.TextFilter import TextFilter
from bot.utils.constants import *


from bot.states.form import Form


def register_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=["start"]))

    dp.message.register(lk_command, TextFilter(LK_BUTTON))
    dp.message.register(get_skins_command, TextFilter(GET_SKINS_BUTTON))
    dp.message.register(invite_friend_command, TextFilter(INVITE_BUTTON))

    dp.message.register(contacts_command, TextFilter(CONTACTS_BUTTON))

    dp.message.register(change_trade_link, TextFilter(TRADE_LINK_BUTTON), Form.lk)
    dp.message.register(back_command, TextFilter(BACK_BUTTON), Form.lk)

    dp.message.register(set_trade_link, Form.trade_link)
    dp.message.register(back_command, TextFilter(BACK_BUTTON), Form.trade_link)

    dp.message.register(confirm_command, TextFilter(AGREE_BUTTON), Form.get_skins)
    dp.message.register(back_command, TextFilter(BACK_BUTTON), Form.get_skins)

    dp.message.register(back_command)
