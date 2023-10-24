import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from keyboards.default.menu import menu, incoming_and_outgoing, cancel


from loader import dp, db


@dp.message_handler(Command("cancel"), state="*")
@dp.message_handler(text="Отмена", state="*")
async def cancel(message: types.Message, state: FSMContext):
    await message.answer("Отменено", reply_markup=menu)
    await state.reset_state()


@dp.message_handler(Command("menu"), state="*")
async def show_menu(message: types.Message, state: FSMContext):
    await message.answer("Выберите действие из меню ниже", reply_markup=menu)
    await state.reset_state()

@dp.message_handler(text="Контакты")
async def select_contacts(message: types.Message):
    contacts = await db.select_contacts()
    user_data = list(contacts)
    count = await db.count_users()
    for i in range(0, count):
        await message.answer(f"{user_data[i][0]}: {user_data[i][1]} 📱 \n"
                             f"Почта: {user_data[i][2]} \n"
                             f"Написать @{user_data[i][3]}", reply_markup=menu)


@dp.message_handler(text="📝Список задач")
async def show_tasks(message: types.Message):
    await message.answer("Выберите входящие или исходящие", reply_markup=incoming_and_outgoing)


@dp.message_handler(content_types=["poll"])
async def msg_with_poll(message: types.Message):
    # question = message.poll.question
    # options = [o.text for o in message.poll.options]
    # anon = message.poll.is_anonymous
    users_id = await db.select_all_telegram_id()
    count = await db.count_users()
    for i in range(0, count):
        await message.forward(chat_id=users_id[i][0])
    # for i in range(0, count):
    #     await dp.bot.send_poll(chat_id=users_id[i][0], question=question, options=options, is_anonymous=anon,
    #                            type=message.poll.type, allows_multiple_answers=message.poll.allows_multiple_answers,
    #                            correct_option_id=message.poll.correct_option_id, explanation=message.poll.explanation,
    #                            open_period=message.poll.open_period, close_date=message.poll.close_date,
    #                            is_closed=message.poll.is_closed)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    contact = message.contact
    phone_number = contact.phone_number
    logging.info(f"contact {message.contact}, phone_number {contact.phone_number}")
    await db.update_user_phone_number(phone_number=phone_number, telegram_id=message.from_user.id)
    # user = await db.select_user(id=message.from_user.id)
    await message.answer(f"Спасибо, {contact.full_name}.\n"
                         f"Твой номер {contact.phone_number} был получен.\n"
                         f"Рекомендуется ввести свою почту командой /email",
                         reply_markup=menu)


@dp.message_handler(text="📢Объявление для всех")
async def ad(message: types.Message, state: FSMContext):
    await message.answer("Введите текст объявления")
    await state.set_state("ad")


@dp.message_handler(state="ad")
async def enter_ad(message: types.Message, state: FSMContext):
    users_id = await db.select_all_telegram_id()
    count = await db.count_users()
    for i in range(0, count):
        logging.info(users_id[i][0])
        await dp.bot.send_message(users_id[i][0], f"{message.from_user.full_name} делает объявление: \n"
                                                  f"{message.text}")
    await message.answer("Объявление сделано!", reply_markup=menu)
    await state.reset_state()
