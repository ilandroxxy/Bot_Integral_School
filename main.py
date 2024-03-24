import asyncio
import string
from config import TOKEN

from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext


import keyboards as kb
import text_handlers as t
from default_commands import *


bot = Bot(token=TOKEN)
dp = Dispatcher()

# todo Убрать все лишнее


class Reg(StatesGroup):
    name = State()
    number = State()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(text=t.text_command_start(message),
                        reply_markup=kb.main)


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer(text=t.text_command_help())


@dp.message(Command('hadm'))
async def cmd_h_adm(message: Message):
    await message.answer_photo(photo='https://disk.yandex.ru/i/Fr7GY-c7fD031Q',
                               caption='Нам очень жаль, что вы столкнулись с ошибкой в боте,'
                                       ' просим вас сообщить о поблеме в личном сообщении нашему администратору.\n'
                                       '⬇️⬇️⬇️',
                               reply_markup=kb.help_admin)


@dp.message(Command('ry8b'))
async def ry_klassb(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAJFP2Xy_XJtKhRXfyI5PZ1EZvEb4WdzAALv1jEbXECZS81ADCRjhTE5AQADAgADeQADNAQ',
                               caption='Расписание уроков 8Б класс\n\n\n'
                                       'Понедельник:\n'
                                       '[8:30 - 9:10]    Разговоры о важном\n[9:20 - 10:00]  Физика\n'
                                       '[10:10 - 10:50]История России\n[11:15 - 11:55]Алгебра\n'
                                       '[12:20 - 13:00]География\n[13:15 - 13:55]Русский язык.\n\n'
                                       'Вторник:\n[8:30 - 9:10]Геометрия\n'
                                       '[9:20 - 10:00]Геометрия\n[10:10 - 10:50]Алгебра\n'
                                       '[11:15 - 11:55]Обществознание\n[12:20 - 13:00]Физкультура\n'
                                       '[13:15 - 13:55]Иностранный язык\n[14:05 - 14:45]Классный час.\n\n'
                                       'Среда:\n[9:20 - 10:00]История Россиии\n'
                                       '[10:10 - 10:50]Физика\n[11:15 - 11:55]Химия\n'
                                       '[12:20 - 13:00]Алгебра\n[13:15 - 13:55]Музыка\n'
                                       '[14:05 - 14:45]Иностранный язык\n\n'
                                       'Четверг:\n[8:30 - 9:10]География\n[9:20 - 10:00]Литература\n'
                                       '[10:10 - 10:50]ОПД\n[11:15 - 11:55]Физкультура\n[12:22 - 13:00]Алгебра\n\n'
                                       'Пятница:\n[8:30 - 9:10]Технология\n[9:20 - 10:00]Русский язык\n'
                                       '[10:10 - 10:50]Биолгия\n[11:15 - 11:55]Физкультура\n'
                                       '[12:20 - 13:00]Информатика\n\n'
                                       'Суббота:\n[8:30 - 9:10]Биология\n[9:20 - 10:00]Иностранный язык\n'
                                       '[10:10 - 10:50]Химия\n[11:15 - 11:55]Русский язык\n'
                                       '[12:20 - 13:00]Литература\n[13:15 - 13:55]ОБЖ.')


@dp.message()
async def messages_handler(message: Message):
    get_message_bot = ' '.join(message.text.lower().split()).strip()
    get_message_bot = get_message_bot.translate(str.maketrans('', '', string.punctuation))

    if get_message_bot == 'расписание':
        await message.answer('Открываю расписания', reply_markup=kb.sche)

    elif get_message_bot == '8б':

        await message.answer_photo(
            photo='AgACAgIAAxkBAAJFP2Xy_XJtKhRXfyI5PZ1EZvEb4WdzAALv1jEbXECZS81ADCRjhTE5AQADAgADeQADNAQ',
            caption='Расписание уроков 8Б класс')

        await message.answer(text='''
    Понедельник:
    [8:30 - 9:10] Разговоры о важном
    [9:20 - 10:00] Физика
    [10:10 - 10:50] История России
    [11:15 - 11:55] Алгебра
    [12:20 - 13:00] География
    [13:15 - 13:55] Русский язык


    Вторник:
    [8:30 - 9:10] Геометрия
    [9:20 - 10:00] Геометрия
    [10:10 - 10:50] Алгебра
    [11:15 - 11:55] Обществознание
    [12:20 - 13:00] Физкультура
    [13:15 - 13:55] Иностранный язык
    [14:05 - 14:45] Классный час


    Среда:
    [9:20 - 10:00] История России
    [10:10 - 10:50] Физика
    [11:15 - 11:55] Химия
    [12:20 - 13:00] Алгебра
    [13:15 - 13:55] Музыка
    [14:05 - 14:45] Иностранный язык


    Четверг:
    [8:30 - 9:10] География
    [9:20 - 10:00] Литература
    [10:10 - 10:50] ОПД
    [11:15 - 11:55] Физкультура
    [12:22 - 13:00] Алгебра


    Пятница:
    [8:30 - 9:10] Технология
    [9:20 - 10:00] Русский язык
    [10:10 - 10:50] Биология
    [11:15 - 11:55] Физкультура
    [12:20 - 13:00] Информатика


    Суббота:
    [8:30 - 9:10] Биология
    [9:20 - 10:00] Иностранный язык
    [10:10 - 10:50] Химия
    [11:15 - 11:55] Русский язык
    [12:20 - 13:00] Литература
    [13:15 - 13:55] ОБЖ
    ''')

    elif get_message_bot == '8а':
        await message.answer('Расписаие 8А класса еще не появилось')

    elif get_message_bot == 'информация':
        await message.answer('Открываю пунтк Информация', reply_markup=kb.info)

    elif get_message_bot == 'о боте':
        await message.answer('Botintegral был создан 15 декабря 2023 года.\n'
                             'Он создан для легкой навигации в школьном процессе.')

    elif get_message_bot == 'связь с администратором':
        await message.answer_photo(photo='https://disk.yandex.ru/i/Fr7GY-c7fD031Q',
                                   caption='Нам очень жаль, что вы столкнулись с ошибкой в боте,'
                                           ' просим вас сообщить о поблеме в личном сообщении нашему администратору.\n'
                                           '⬇️⬇️⬇️',
                                   reply_markup=kb.help_admin)
    elif get_message_bot == 'доп занятия':
        await message.answer('Открываю пункт Дополнительные занятия', reply_markup=kb.addclass)

    elif get_message_bot == 'другое':
        await message.answer('Открываю меню Другое', reply_markup=kb.other)
        await message.answer('Эта кнопка на этапе разработки')

    # todo Добавить обработчки для команд шаг назад
    elif get_message_bot in ('назад', 'отменить', 'шаг назад', 'предыдущий', '⬅️'):
        await message.answer('◀️Назад', reply_markup=kb.main)

'''


@dp.message(F.text == 'student')
async def how_are_you(message: Message):
    await message.answer('Ок!', reply_markup=await kb.inline_student())



@dp.message(F.text == 'Дополнительные уроки')
async def dop_yrok(message: Message):
    await message.answer('Открываю меню Дополнительные уроки', reply_markup=kb.dop_yrok)
    await message.answer('Меню Дополнительные уроки находится на этапе разработки')



@dp.message(F.text == 'Секции')
async def schedule(message: Message):
    await message.answer('Эта кнопка на этапе разработки')




@dp.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f'ID фото: {message.photo[-1].file_id}')


@dp.message(Command('get_photo'))
async def get_photo(message: Message):
    await message.answer_photo(photo='https://disk.yandex.ru/i/Fr7GY-c7fD031Q',
                               caption='Нам очень жаль, что вы столкнулись с ошибкой в боте,'
                                       ' просим вас сообщить о поблеме в личном сообщении нашему администратору',
                               reply_markup=kb.help_admin)


@dp.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer('Рады что вы решили зарегистрироватся в нашем боте!')
    await message.answer('Введите Ваше имя\nНапример: Иван')


@dp.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.number)
    await message.answer('Введите номер телефона\nВ формате +7XXXXXXXXXX')


@dp.message(Reg.number)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f'Спасибо, регистрация завершина.\nИмя: {data["name"]}\nНомер: {data["number"]}')
    await state.clear()
'''

async def main():
    await set_bot_commands(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())