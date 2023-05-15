from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefonlar'),
            KeyboardButton(text='Kampyuter')
        ],
        [
            KeyboardButton(text='Mayishiy texnika'),
            KeyboardButton(text='Aksesuarlar')
        ]
    ],
    resize_keyboard=True
)