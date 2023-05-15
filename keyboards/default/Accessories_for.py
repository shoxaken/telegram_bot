from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

accessories_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Hours'),
            KeyboardButton(text='Perfume')
        ],
        [
            KeyboardButton(text='iphon'),
            KeyboardButton(text='back')
        ]
    ],
    resize_keyboard=True
)