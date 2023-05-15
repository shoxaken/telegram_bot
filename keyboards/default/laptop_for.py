from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

laptop_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Lenovo'),
            KeyboardButton(text='Samsung')
        ],
        [
            KeyboardButton(text='Macbook'),
            KeyboardButton(text='back')
        ]
    ],
    resize_keyboard=True
)