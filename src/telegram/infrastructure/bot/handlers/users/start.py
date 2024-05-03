from dependency_injector.wiring import Provide, inject
from aiogram import Router, filters, types
from aiogram.utils.text_decorations import html_decoration

from src.containers import AppContainer
from src.telegram.infrastructure.bot.misc import commands, icons
from src.telegram.infrastructure.bot.pages import Page


router = Router()


@router.message(filters.Command(commands=[commands.START_CMD]))
@inject
async def on_start(
        message: types.Message,
        # client_service: TelegramClientService = Provide[AppContainer.client.service],
):
    # client_user = await client_service.get_me()
    await Page(
        icon=icons.person,
        title=message.from_user.username,
        content=html_decoration.pre_language(message.from_user.model_dump(), 'JSON'),
    ).answer(message)

