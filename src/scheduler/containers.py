from dependency_injector import containers, providers

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger


async def scheduler_init(scheduler: AsyncIOScheduler):
    from . import tasks

    scheduler.add_job(tasks.get_me_task, IntervalTrigger(seconds=5))

    yield scheduler.start()
    scheduler.shutdown()


class SchedulerContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[])

    scheduler = providers.Singleton(AsyncIOScheduler)
    __scheduler_init = providers.Resource(scheduler_init, scheduler=scheduler)
