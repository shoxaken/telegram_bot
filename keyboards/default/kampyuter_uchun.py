from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

kampyuter_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Lenovo'),
            KeyboardButton(text='Samsung')
        ],
        [
            KeyboardButton(text='Macbook'),
            KeyboardButton(text='orqaga')
        ]
    ],
    resize_keyboard=True
)