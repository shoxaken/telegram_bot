from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
menu_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Iphone'),
            KeyboardButton(text='Laptop')
        ],
        [
            KeyboardButton(text='Household appliances'),
            KeyboardButton(text='Accessories')
        ]
    ],
    resize_keyboard=True
)