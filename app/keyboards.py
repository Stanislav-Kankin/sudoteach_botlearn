from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton,
    InlineKeyboardMarkup, InlineKeyboardButton)


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
