import asyncio

from dependency_injector import containers, providers

from aiogram import Bot, Dispatcher

from src.config.settings import TelegramSettings
from src.telegram.infrastructure.bot.misc import commands


async def bot_start(dp: Dispatcher, bot: Bot):
    from src.telegram.infrastructure.bot import handlers
    handlers.register(dp)

    await commands.set_bot_commands(bot)

    # pooling is block func, to avoid this run as task, otherwise use webhook's
    asyncio.ensure_future(dp.start_polling(bot, handle_signals=False))

    yield
    await dp.stop_polling()


class TelegramContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[
        'src.scheduler.tasks'
    ])

    config = providers.Dependency(TelegramSettings)

    dispatcher = providers.Singleton(Dispatcher)
    bot = providers.Singleton(
        Bot,
        token=config.provided.bot_token,
        parse_mode='HTML',
    )
    __bot_start = providers.Resource(bot_start, dp=dispatcher, bot=bot)
