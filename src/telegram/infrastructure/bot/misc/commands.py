from aiogram import Bot, types

from . import icons

START_CMD = 'start'
HELP_CMD = 'help'

BOT_COMMANDS = {
    HELP_CMD: ' '.join([icons.white_quest, 'Помогите']),
}


async def set_bot_commands(bot: Bot) -> None:
    commands = [types.BotCommand(command=c, description=d) for c, d in BOT_COMMANDS.items()]
    await bot.set_my_commands(commands=commands, scope=types.BotCommandScopeAllPrivateChats())
