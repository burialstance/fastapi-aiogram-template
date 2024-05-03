from aiogram import Router, filters, types

from src.bot.infrastructure.bot.pages import WarningPage

router = Router()


@router.error(filters.ExceptionTypeFilter(BaseAPIException))
async def on_api_base_exc(error: types.ErrorEvent):
    warning_page = WarningPage(
        title='Service unavailable',
        content='Please try later..',
    )

    event = error.update.event
    match type(event):
        case types.CallbackQuery:
            await event.answer()
            await event.message.answer(warning_page.build_text())
        case _:
            await event.bot.send_message(error.update.message.from_user.id, warning_page.build_text())

    raise error.exception
