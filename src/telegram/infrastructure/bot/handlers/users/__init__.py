from aiogram import Router

from . import start
from . import help

router = Router()
router.include_router(start.router)
router.include_router(help.router)

