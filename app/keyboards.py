from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton,)

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Корзина'), KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Контакты')]
], resize_keyboard=True, input_field_placeholder='ВЫБЕРИТЕ КНОПКУ НИЖЕ!!!')

inline_main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(
        text='Контакты',
        callback_data='contact'
    )],
    [InlineKeyboardButton(
        text='Корзина',
        callback_data='basket'
    )]
])


async def catalog() -> None:
    all_data = (
        'Nissan', 'Lada', 'BMW',
        'Lexus', 'China_cars',
        'Motoroller', 'TEST'
    )

    keyboard = ReplyKeyboardBuilder()

    for data in all_data:
        keyboard.add(KeyboardButton(text=data))
    return keyboard.adjust(2).as_markup(resize_keyboard=True)
