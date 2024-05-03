from dependency_injector import containers, providers

from src.config import settings
from src.db.containers import DatabaseContainer

from src.telegram.containers import TelegramContainer
from src.scheduler.containers import SchedulerContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[])

    database = providers.Container(DatabaseContainer, config=settings.db)
    scheduler = providers.Container(SchedulerContainer)
    telegram = providers.Container(TelegramContainer, config=settings.telegram)
