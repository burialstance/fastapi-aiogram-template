from pprint import pprint

from aiogram import Bot
from dependency_injector.wiring import inject, Provide

from src.telegram.containers import TelegramContainer


@inject
async def get_me_task(bot: Bot = Provide[TelegramContainer.bot]):
    pprint(
        (await bot.get_me()).model_dump()
    )
