from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from random import choice


def random_back():
    return choice(['Назад', 'Отменить', 'Шаг назад', 'Предыдущий', 'Undo', '⬅️'])


# меню после команды /start
main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Расписание')], [KeyboardButton(text='Информация')],
    [KeyboardButton(text='Доп. занятия')], [KeyboardButton(text='Другое')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

# меню на кнопку Информация
info = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='О боте')],
    [KeyboardButton(text='Связь с администратором')],
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

# меню на кнопку Расписание
# todo Пример того, как можно оформлять клавиатуру по несколько кнопок в строке
sche = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='8А'), KeyboardButton(text='8Б')],
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


# меню на кнопку Доп. занятия
addclass = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Дополнительные уроки')], [KeyboardButton(text='Секции')],
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')

# меню на кнопку Доп уроки в разделе Доп. занятия
dop_yrok = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Доп. уроки по физике')], [KeyboardButton(text='Доп. уроки по химии')],
    [KeyboardButton(text='Доп. уроки по русскому языку')],
    [KeyboardButton(text='Доп. уроки по математике')], [KeyboardButton(text='Доп. уроки по история')],
    [KeyboardButton(text='Доп. уроки по обществознанию')], [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


# меню на кнопку Другое
other = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text=f'{random_back()}')]
],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню.')


settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='YouTube', url='https://www.youtube.com/')]
    ])

# меню на кнопку Связь с администратором и на команду /hadm
help_admin = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/Kostaborodin')],
    [InlineKeyboardButton(text='VK', url='https://vk.com/id659392062')]
    ])


student = ['биба', 'боба', 'вова', 'коля', 'володя', 'сергей']


async def inline_student():
    keyboard = InlineKeyboardBuilder()
    for car in student:
        keyboard.add(InlineKeyboardButton(text=car, url='https://www.youtube.com/'))
    return keyboard.adjust(2).as_markup()