from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery

from keyboards.default.menu_uchun import menu_buttons
from keyboards.default.for_menu import menu_button
from keyboards.default.telefon_uchun import telefonlar_buttons
from keyboards.default.kampyuter_uchun import kampyuter_buttons
from keyboards.default.Mayishiy_texnika_uchun import mayishiy_buttons
from keyboards.default.Aksesuarlar import aksesuarlar_buttons
from keyboards.inline.tillar_uchun import tillar_buttons
from keyboards.default.Accessories_for import accessories_buttons
from keyboards.default.laptop_for import laptop_buttons
from keyboards.default.Iphone_fon import iphone_buttons
from keyboards.default.Household_appliances_for import Household_buttons
from loader import dp

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!",reply_markup=tillar_buttons)

@dp.message_handler(text='Kampyuter')
async def bot_start(message: types.Message):
    await message.answer(f"Kampyuterlar tanlang, {message.from_user.full_name}!",reply_markup=kampyuter_buttons )

@dp.message_handler(text='Telefonlar')
async def bot_start(message: types.Message):
    await message.answer(f"Telefonlarni tanlang, {message.from_user.full_name}!",reply_markup=telefonlar_buttons )

@dp.message_handler(text='Mayishiy texnika')
async def bot_start(message: types.Message):
    await message.answer(f"Mayishiy texnika tanlang, {message.from_user.full_name}!",reply_markup=mayishiy_buttons )


@dp.message_handler(text='Aksesuarlar')
async def bot_start(message: types.Message):
    await message.answer(f"Mayishiy texnika tanlang, {message.from_user.full_name}!",reply_markup=aksesuarlar_buttons )

@dp.callback_query_handler(text="til1")
async def bot_start(xabarlar: CallbackQuery):
    await xabarlar.message.answer(f"menu tanlang, ", reply_markup=menu_buttons)

@dp.callback_query_handler(text="til2")
async def bot_start(xabarlar: CallbackQuery):
    await xabarlar.message.answer(f"menu choose, ", reply_markup=menu_button)

@dp.message_handler(text='Accessories')
async def bot_start(message: types.Message):
    await message.answer(f"Accessories texnika tanlang, {message.from_user.full_name}!",reply_markup=accessories_buttons )

@dp.message_handler(text='Laptop')
async def bot_start(message: types.Message):
    await message.answer(f"Laptop choose a technique, {message.from_user.full_name}!",reply_markup=laptop_buttons)

@dp.message_handler(text='Iphone')
async def bot_start(message: types.Message):
    await message.answer(f"Iphon choose a technique, {message.from_user.full_name}!",reply_markup=iphone_buttons)

@dp.message_handler(text='Household appliances')
async def bot_start(message: types.Message):
    await message.answer(f"Iphon choose a technique, {message.from_user.full_name}!",reply_markup=Household_buttons)

@dp.message_handler(text='orqaga')
async def bot_start(message: types.Message):
    await message.answer(f"Orqaga qaytingiz, {message.from_user.full_name}!",reply_markup=menu_buttons )

@dp.message_handler(text='back')
async def bot_start(message: types.Message):
    await message.answer(f"go back, {message.from_user.full_name}!",reply_markup=menu_button)

@dp.message_handler(commands="boshlash")
async def bot_start(message: types.Message):
    await message.answer(f"Salom,botga hush kelibsi!")
