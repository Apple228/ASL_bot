from aiogram import types
import logging
from aiogram.dispatcher.filters import Command

from keyboards.default.menu import menu
from loader import dp, db


@dp.message_handler(Command("contact"))
async def select_contacts(message: types.Message):
    contacts = await db.select_contacts()
    user_data = list(contacts)
    count = await db.count_users()
    for i in range(0, count):
        await message.answer(f"{user_data[i][0]}:{user_data[i][1]}📞", reply_markup=menu)
