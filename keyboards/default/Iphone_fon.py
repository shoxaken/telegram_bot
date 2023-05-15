from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

iphone_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Redmi'),
            KeyboardButton(text='Samsung')
        ],
        [
            KeyboardButton(text='iphon'),
            KeyboardButton(text='back')
        ]
    ],
    resize_keyboard=True
)