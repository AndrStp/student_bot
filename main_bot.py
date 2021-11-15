import asyncio
from aiogram import Bot, Dispatcher, executor

from secret import BOT_TOKEN


API_TOKEN = BOT_TOKEN

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)