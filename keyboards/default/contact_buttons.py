from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

phone_number = ReplyKeyboardMarkup(resize_keyboard=True,
                                   keyboard=[
                                       [
                                           KeyboardButton(text="📱",
                                                          request_contact=True)
                                       ]
                                   ])
