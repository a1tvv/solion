import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer("Здравствуйте! Для заказа нажмите /basket")


@dp.message(Command('basket'))
async def basket(message: types.Message):
    await message.answer(
        "Отлично! Пожалуйста, отправьте одним сообщением:\n"
        "1. Ваше имя\n"
        "2. Что вы хотите заказать\n"
        "3. Время доставки (от 30 минут)\n\n"
        "Пример:\n"
        "Иван\n"
        "Пицца Маргарита\n"
        "15:00\n\n"
        '* Если ваше сообщение не обработалась, отправьте обратно'
    )


# Обработчик для получения заказа
@dp.message()
async def process_order(message: types.Message):
    if not message.text.startswith('/'):
        # Создаем inline-кнопки
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text='Посмотреть Статус Заказа', callback_data='check_status')],
                [InlineKeyboardButton(text='Очистить чат', callback_data='clear_chat')]
            ]
        )

        # Отправляем ответ вместе с inline-кнопками
        await message.answer(
            f"✅ Ваш заказ принят!\n\n{message.text}\n\nОжидайте подтверждения!",
            reply_markup=keyboard
        )
    else:
        await message.answer("Пожалуйста, используйте команды:\n/start - начать\n/basket - оформить заказ")


# Обработчик нажатий на inline-кнопки
@dp.callback_query()
async def handle_callback(callback: types.CallbackQuery):
    if callback.data == 'check_status':
        await callback.message.answer("Статус вашего заказа: В обработке")
    elif callback.data == 'clear_chat':
        await callback.message.answer("Чо такой крутой да? В ручную очищай!")

    # Подтверждаем нажатие кнопки
    await callback.answer()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())