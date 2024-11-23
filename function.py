import os


from aiogram import Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboard import location_contact_button, channel_list
from keyboard import menu_button




async def register_location(message:Message,bot:Bot, state:FSMContext):
    chat_id=os.getenv("CHAT_ID")
    await print(message.location.latitude,message.location.longitude)
    await bot.send_location(chat_id=chat_id,latitude=message.location.latitude,longitude=message.location.longitude)
    await message.answer(text="Lokatsiya yuborildi")
async def check_join(message: Message, bot: Bot, state: FSMContext):
    await message.answer("Botimizdan foydalanish uchun kanalga a'zo bo'ling !!!",reply_markup=channel_list)
#await message.answer("Botimizdan foydalanish uchun<a href='https://t.me/+FRmSvt0qKsExMDMy' >kanalga a'zo bo'linglar </a> qo'shiling",
#                     parse_mode='html')



async def start_menu(message:Message,bot:Bot, state:FSMContext):


    await message.answer("Menulardan birini tanlang", reply_markup=menu_button)


async def check_channel_joined(massage: Message, *args, **kwargs):
    await massage.answer("Qaytadan startni bosing")

async def echo(message:Message,bot:Bot,state:FSMContext):
    await message.copy_to(chat_id=message.from_user.id)
async def register_contact(message:Message,bot:Bot,state:FSMContext):
    chat_id = os.getenv("CHAT_ID")
    await bot.send_contact(chat_id=chat_id, phone_number=message.contact.phone_number,first_name=message.contact.first_name)
    await message.answer(text="Kontaktingiz adminga yuborildi tez orada aloqaga chiqamiz!")

'''
async def info(message: Message, bot: Bot, state: FSMContext):
  profile= await bot.get_chat(chat_id=message.from_user.id)
  user =message.from_user
  data= f"""Sizning ismingiz:{user.first_name},Id raqamingiz:{user.id} \n"""
  if user.username :
      data+=f"Sizning usernamengiz @{user.username}\n"

  if user.last_name:
      data +=f"Sizning famalyangiz {user.last_name}\n"
  if profile.bio:
      data+=f"sizning bioingiz  {profile.bio}\n"
  pprint(data)
  await message.answer(text=data)
  '''



async def share_menu(message:Message,bot:Bot, state:FSMContext):
    await message.answer("Ma'lumotlarni birini tanlang", reply_markup=location_contact_button)
async def start(bot: Bot):
    await bot.send_message(chat_id="1855391044", text="Bot ishga tushdi✅")

async def stop(bot:Bot):
    await bot.send_message(chat_id="1855391044", text="Bot to'xtadi⚠️")