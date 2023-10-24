import logging
from datetime import datetime

from aiogram import executor, Dispatcher
from loader import dp, db, scheduler
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands




async def on_startup(dispatcher):
    # Уведомляет про запуск
    logging.info("Создаем подключение к базе данных")
    await db.create_users()
    logging.info("Создаем таблицу пользователей")
    await db.create_table_users()
    logging.info("Готово.")
    await on_startup_notify(dispatcher)
    # scheduler_jobs()
    await set_default_commands(dp)


if __name__ == '__main__':
    scheduler.start()
    executor.start_polling(dp, on_startup=on_startup)
