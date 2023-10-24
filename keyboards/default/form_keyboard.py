from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


start_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="📝Новый лид"),
                                         ]
                                     ])

have_area_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="Есть"),
                                             KeyboardButton(text="Нет"),
                                         ]
                                     ])
construction_technology_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="Каменный"),
                                             KeyboardButton(text="Клееный брус"),

                                         ],
                                         [
                                             KeyboardButton(text="Бревно"),
                                             KeyboardButton(text="Каркасный"),
                                         ],
                                         [
                                             KeyboardButton(text = "PREFAB"),

                                         ]
                                     ])
prod_line_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="IZBURG"),
                                             KeyboardButton(text="LIVVIL"),
                                         ],
                                         [
                                             KeyboardButton(text = "Индивидуальный")
                                         ]
                                     ])

source_of_financing_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                     keyboard=[
                                         [
                                             KeyboardButton(text="Личные"),
                                             KeyboardButton(text="Ипотека"),

                                         ],
                                         [
                                             KeyboardButton(text="Сбербанк"),
                                             KeyboardButton(text="Дом РФ"),
                                         ],
                                     ])


planing_build_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                             keyboard=[
                                                 [
                                                     KeyboardButton(text="2023"),
                                                     KeyboardButton(text="1-я половина 2024"),
                                                 ],
                                                 [
                                                     KeyboardButton(text="2025"),
                                                     KeyboardButton(text="2-я половина 2024")
                                                 ]
                                             ])

skip_email_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                             keyboard=[
                                                 [
                                                     KeyboardButton(text="Пропустить"),
                                                 ],

                                             ])

messengers_list_keyboard = ReplyKeyboardMarkup(resize_keyboard=True,
                                             keyboard=[
                                                 [
                                                     KeyboardButton(text="Почта"),
                                                     KeyboardButton(text="Телефон"),
                                                 ],
                                                 [
                                                     KeyboardButton(text="Телеграмм"),
                                                     KeyboardButton(text="Вотсап")
                                                 ]
                                             ])