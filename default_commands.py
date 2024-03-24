from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeAllPrivateChats


# todo Дописать свои команды в меню команд
async def set_bot_commands(bot: Bot):
    custom_commands = [
        BotCommand(command="homework", description="Конструктор домашних заданий для моих учеников 🎓"),
        BotCommand(command="mylessons", description="Проверить кол-во занятий в абонементе 🧮 "),
        BotCommand(command="price", description="Получить информацию о ценах и реквизиты 💸"),
        BotCommand(command="useful", description="Шпаргалки от Яндекс Практикум по Python 🐍"),
        BotCommand(command="getmyid", description="Бот покажет ваш id пользователя Telegram 👾"),
        BotCommand(command="download", description="Список программ которые понадобятся для уроков 📎"),
        BotCommand(command="start", description="Перезапуск бота, на стартовую позицию 🏁")

    ]

    await bot.set_my_commands(
        commands=custom_commands, scope=BotCommandScopeAllPrivateChats()
    )