import os
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio

TOKEN = "9026515987:AAHZgh3CZIKmLbdCmlTVY9y15SFqZpydLz8"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        "Assalomu alaykum! Slayd yasab beruvchi botimizga xush kelibsiz.\n"
        "Hozircha serverga muvaffaqiyatli ulandim! Tez orada slayd tayyorlash funksiyalari qo‘shiladi."
    )

async def main():
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
