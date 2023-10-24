from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("cancel", "Отмена действия"),
        types.BotCommand("menu", "Вернуться в меню"),
        types.BotCommand("cancel", "Отменить"),
    ])
