from aiogram import Router

from . import api

router = Router()
router.include_router(api.router)
