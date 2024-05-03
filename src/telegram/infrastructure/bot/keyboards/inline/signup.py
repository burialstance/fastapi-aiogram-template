import enum
from typing import Optional

from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, InlineKeyboardMarkup

from src.telegram.infrastructure.bot.misc import icons


class SignupAction(str, enum.Enum):
    start = 'start'


class SignupCallback(CallbackData, prefix='signup'):
    action: SignupAction
    payload: Optional[str] = None


def build_start_signup_kb() -> InlineKeyboardMarkup:
    kb = InlineKeyboardBuilder()
    kb.add(
        InlineKeyboardButton(
            text=' '.join([icons.person, 'Познакомимся?']),
            callback_data=SignupCallback(action=SignupAction.start).pack()
        )
    )
    return kb.adjust(1).as_markup()
