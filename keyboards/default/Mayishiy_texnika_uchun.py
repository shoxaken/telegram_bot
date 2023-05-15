from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

mayishiy_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='artel'),
            KeyboardButton(text='Samsung')
        ],
        [
            KeyboardButton(text='LG'),
            KeyboardButton(text='orqaga')
        ]
    ],
    resize_keyboard=True
)