import os
from asyncio import run
from aiogram import F

from aiogram.types import Message, BotCommand
from dotenv import load_dotenv
from aiogram.filters import Command, CommandStart
from function import start, check_join, stop, start_menu, share_menu, register_location, register_contact, \
    check_channel_joined
from filtes import CheckSubFilter
from aiogram import Bot, Dispatcher

load_dotenv()


TOKEN = os.getenv("BOT_TOKEN")

dp = Dispatcher()



async def main(dp) -> None:
    bot = Bot(token=TOKEN, skip_update=True)


    await bot.set_my_commands(
        [
          BotCommand(command="/start", description="Bot ni ishga tushurildi"),
          BotCommand(command="/share",description="Ma'motlaringni yuborish")
        ]
    )
    dp.startup.register(start)
    dp.message.register(check_join,CheckSubFilter())
    dp.callback_query.register(check_channel_joined, F.data == "check_subsciption")
    dp.message.register(start_menu,CommandStart())
    dp.message.register(register_location, F.location)
    dp.message.register(register_contact, F.contact)
    dp.message.register(share_menu,Command("share"))


    dp.shutdown.register(stop)
    await dp.start_polling(bot)

if __name__ == "__main__":
    run(main(dp))
