from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📄Документы"),
            KeyboardButton(text="📢Объявление для всех")
        ],
        [
            KeyboardButton(text="📝Новый лид")
        ]
    ],
    resize_keyboard=True
)


incoming_and_outgoing = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="📤Исходящие")
        ],
        [
            KeyboardButton(text="📥Входящие")
        ]

    ],
    resize_keyboard=True
)


cancel = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Отмена")
        ]
    ],
    resize_keyboard=True
)

