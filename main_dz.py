import asyncio
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import TOKEN
# import keyboards as kb
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()


def get_cat_image(status_code):
    url = f"https://http.cat/{status_code}"
    print(url)
    response = requests.get(url)
    return url


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer('Привет! Лови смешную фотку')
    status_code = random.randint(100, 599)
    print(status_code)
    photo = get_cat_image(status_code)
    if photo:
        await message.answer_photo(photo=photo)
    else:
        await message.answer("Не удалось найти картинку для этого статуса. Попробуйте снова!")


async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   asyncio.run(main())
