from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

telefonlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Redmi'),
            KeyboardButton(text='Samsung')
        ],
        [
            KeyboardButton(text='iphon'),
            KeyboardButton(text='orqaga')
        ]
    ],
    resize_keyboard=True
)