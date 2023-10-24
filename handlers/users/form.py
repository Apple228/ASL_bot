import datetime

import requests
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Command
from aiogram.types import ReplyKeyboardRemove

from data.config import PATH
from keyboards.default.menu import menu

from loader import dp
from google.oauth2.service_account import Credentials
import gspread_asyncio


def get_scoped_credentials(path: str):
    creds = Credentials.from_service_account_file(path)

    def prepare_scoped_credentials():
        return creds.with_scopes(
            ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
        )

    return prepare_scoped_credentials


async def create_spreadsheet(client, spreadsheet_name) -> gspread_asyncio.AsyncioGspreadSpreadsheet:
    spreadsheet = await client.create(spreadsheet_name)
    spreadsheet = await client.open_by_key(spreadsheet.id)
    return spreadsheet


async def add_worksheet(async_spreadsheet: gspread_asyncio.AsyncioGspreadSpreadsheet, worksheet_name):
    worksheet = await async_spreadsheet.add_worksheet(worksheet_name, 500, 500)
    worksheet = await async_spreadsheet.worksheet(worksheet.title)
    return worksheet


@dp.message_handler(text='📝Новый лид')
async def bot_start(message: types.Message, state: FSMContext):
    await message.answer("Номер телефона", reply_markup=ReplyKeyboardRemove())
    await state.set_state("Номер телефона")


@dp.message_handler(state="Номер телефона")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_phone_number = message.text
    await state.update_data(client_phone_number=client_phone_number)
    await message.answer("Имя")
    await state.set_state("Имя")


@dp.message_handler(state="Имя")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    client_name = message.text
    await state.update_data(client_name=client_name)
    await message.answer("Название компании")
    await state.set_state("Название компании")


@dp.message_handler(state="Название компании")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    company_name = message.text
    await state.update_data(company_name=company_name)
    await message.answer("Комментарий")
    await state.set_state("Комментарий")


@dp.message_handler(Command("stop"), state='*')
@dp.message_handler(state="Комментарий")
async def state_data_gsheets(message: types.Message, state: FSMContext):
    if message.text == "/stop":
        comment = ""
    else:
        comment = message.text
    await state.update_data(comment=comment)

    data = await state.get_data()
    today = datetime.date.today()

    await message.answer(f"1. {message.from_user.full_name}\n"
                         f"2. {today.strftime('%d.%m.%y')}\n"
                         f"3. Номер телефона: {data.get('client_phone_number')}\n"
                         f"4. Имя: {data.get('client_name')}\n"
                         f"5. Название компании: {data.get('company_name')}\n"
                         f"6. Комментарий: {data.get('comment')}\n",
                         reply_markup=menu)
    await state.reset_state()
    spreadsheet_id = '1is59jF6zqLMV5UHsqzT30Ee3OBo74U0_nA7n23q8k1g'
    client = gspread_asyncio.AsyncioGspreadClientManager(get_scoped_credentials(PATH))  # импорт из конфига
    client = await client.authorize()
    async_spreadsheet = await client.open_by_key(spreadsheet_id)

    worksheet = await async_spreadsheet.worksheet('Лист1')
    values = [
        message.from_user.full_name,
        today.strftime('%d.%m.%y'),
        data.get('client_phone_number'),
        data.get('client_name'),
        data.get('company_name'),
        data.get('comment')
    ]
    await worksheet.append_row(values)
