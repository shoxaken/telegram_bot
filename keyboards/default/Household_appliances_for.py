from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

Household_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='artel'),
            KeyboardButton(text='Samsung')
        ],
        [
            KeyboardButton(text='LG'),
            KeyboardButton(text='back')
        ]
    ],
    resize_keyboard=True
)