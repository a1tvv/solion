import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

user_tasks = {}  # Исправлено: было user_task

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Добавить задачу')],
        [KeyboardButton(text='Мои задачи')],
        [KeyboardButton(text='Очистить задачи')]
    ],
    resize_keyboard=True
)


@dp.message(Command('todo'))
async def todo(message: types.Message):
    await message.answer('To Do', reply_markup=keyboard)


@dp.message(lambda msg: msg.text == 'Добавить задачу')
async def ask_task(message: types.Message):
    await message.answer('Напиши свою задачу')


@dp.message(lambda msg: not msg.text.startswith('/'))  # Исправлено: startswich → startswith
async def save_task(message: types.Message):
    text = message.text

    if text in {'Добавить задачу', 'Мои задачи', 'Очистить задачи'}:
        return

    user_id = message.from_user.id

    if user_id not in user_tasks:  # Исправлено: user_task → user_tasks
        user_tasks[user_id] = []

    user_tasks[user_id].append(text)  # Исправлено: user_task → user_tasks
    await message.answer(f'Задача добавлена:\n {text}')  # Исправлено: \m → \n


# Мои задачи
@dp.message(lambda msg: msg.text == 'Мои задачи')
async def show_task(message: types.Message):
    user_id = message.from_user.id
    tasks = user_tasks.get(user_id, [])  # Исправлено: переменная task → tasks

    if not tasks:  # Исправлено: task → tasks
        await message.answer('У тебя нет задач')
        return

    text = 'Твои задачи: \n\n'
    for i, task in enumerate(tasks, 1):  # Исправлено: task → tasks
        text += f'{i}. {task}\n'  # Исправлено: , → .

    await message.answer(text)


# Очистить задачи
@dp.message(lambda msg: msg.text == 'Очистить задачи')  # Исправлено: добавил msg.
async def clear_task(message: types.Message):
    user_id = message.from_user.id
    user_tasks[user_id] = []  # Исправлено: user_task → user_tasks
    await message.answer('Все задачи очищены!')  # Добавлено подтверждение


# Команда start
@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привет, это weather bot!')


# Команда help
@dp.message(Command('help'))
async def help_message(message: types.Message):
    await message.answer('Ничем не могу помочь, иди в лес')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())