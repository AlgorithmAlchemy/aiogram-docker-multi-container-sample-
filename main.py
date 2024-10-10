import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio

# Логирование
logging.basicConfig(level=logging.INFO)


class BotApp:
    def __init__(self, token):
        # Инициализация бота и диспетчера
        self.bot = Bot(token=token)
        self.dp = Dispatcher()

        # Настройка кнопочной и инлайн клавиатур
        self.reply_keyboard = self.create_reply_keyboard()
        self.inline_kb = self.create_inline_keyboard()

        # Регистрация хендлеров
        self.register_handlers()

    def create_reply_keyboard(self):
        """Создает обычную кнопочную клавиатуру."""
        button_how_are_you = KeyboardButton(text='Как дела?')
        button_inline_example = KeyboardButton(text='Инлайн-кнопки')
        keyboard = [[button_how_are_you, button_inline_example]]  # Обернули кнопки в список списков
        return ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

    def create_inline_keyboard(self):
        """Создает инлайн-клавиатуру."""
        inline_btn_1 = InlineKeyboardButton(text='Хорошо', callback_data='good')
        inline_btn_2 = InlineKeyboardButton(text='Не очень', callback_data='bad')
        inline_btn_url = InlineKeyboardButton(text='Открой Google', url='https://www.google.com')

        # Кнопки должны быть переданы в список списков
        inline_kb = InlineKeyboardMarkup(inline_keyboard=[
            [inline_btn_1, inline_btn_2],  # Две кнопки в одной строке
            [inline_btn_url]  # Одна кнопка в другой строке
        ])

        return inline_kb

    async def on_message(self, message: types.Message):
        """Обрабатывает входящие сообщения."""
        if message.text == 'Как дела?':
            await message.answer("У меня всё отлично, спасибо! А у тебя?")
        elif message.text == 'Инлайн-кнопки':
            await message.answer("Выбери один из вариантов:", reply_markup=self.inline_kb)
        else:
            await message.answer("Привет! Как у тебя дела?", reply_markup=self.reply_keyboard)

    async def on_callback_query(self, callback_query: types.CallbackQuery):
        """Обрабатывает инлайн-кнопки."""
        if callback_query.data == 'good':
            await callback_query.answer(text="Рад, что у тебя всё хорошо!")
        elif callback_query.data == 'bad':
            await callback_query.answer(text="Надеюсь, всё скоро наладится!")

    def register_handlers(self):
        """Регистрация хендлеров."""
        self.dp.message.register(self.on_message)
        self.dp.callback_query.register(self.on_callback_query, lambda c: c.data in ['good', 'bad'])

    async def run(self):
        """Запуск бота."""
        await self.dp.start_polling(self.bot)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <API_TOKEN>")
        sys.exit(1)

    API_TOKEN = sys.argv[1]  # Получаем токен из аргументов
    bot_app = BotApp(token=API_TOKEN)
    asyncio.run(bot_app.run())