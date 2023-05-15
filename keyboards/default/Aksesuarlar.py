from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

aksesuarlar_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Soatlar'),
            KeyboardButton(text='Atrlar')
        ],
        [
            KeyboardButton(text='Telefonlar'),
            KeyboardButton(text='orqaga')
        ]
    ],
    resize_keyboard=True
)