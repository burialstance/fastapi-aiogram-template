from aiogram import Router, Dispatcher

from . import users
# from . import errors

router = Router()
router.include_router(users.router)
# router.include_router(errors.router)


def register(dispatcher: Dispatcher):
    dispatcher.include_router(router)
