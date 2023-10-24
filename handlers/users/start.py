import logging

import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import contact_buttons
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    logging.info(f"""telegram_id={message.from_user.id},
                      full_name={message.from_user.full_name},
                      username={message.from_user.username}""")
    try:
        await db.add_user(telegram_id=message.from_user.id,
                          full_name=message.from_user.full_name,
                          username=message.from_user.username)

    except asyncpg.exceptions.UniqueViolationError:
        await db.select_user(telegram_id=message.from_user.id)

    count = await db.count_users()

    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Ты был занесен в базу',
                f'В базе <b>{count}</b> пользовател'+(
        'ей' if count % 10 == 0 or 4 < count % 10 < 10 or 10 < count % 100 < 15 else 'я'
        if 1 < count % 10 < 5 else 'ь'),
                "Нажми пожалуста на кнопку ниже,",
                "чтобы поделиться своим номером"


            ]), reply_markup=contact_buttons.phone_number)
