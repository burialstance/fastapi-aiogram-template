from aiogram import Router, filters, types
from aiogram.fsm.context import FSMContext

from src.telegram.infrastructure.bot.misc import commands, icons
from src.telegram.infrastructure.bot.pages import Page

router = Router()


def get_stupid_desc() -> str:
    import random
    items = [
        'Лучше жопа в мыле, чем мыло в жопе.',
        'Взял нож - режь, взял дошик - ешь.',
        'Никогда не сдавайтесь, идите к своей цели! А если будет сложно – сдавайтесь.',
        'Всего одна ошибка – и ты ошибся.',
        'Делай, как надо. Как не надо, не делай.',
        'Как говорил мой дед, «Я твой дед».'
    ]
    return '\n'.join([random.choice(items), '(с) json стетхем'])


@router.message(filters.Command(commands=[commands.HELP_CMD]))
async def on_help(message: types.Message, state: FSMContext):
    await Page(
        icon=icons.info,
        title='Help',
        content='',
        desc=get_stupid_desc(),
        reply_markup=None
    ).answer(message)
