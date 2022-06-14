import logging
from knopki import *
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
API_TOKEN = '5576038444:AAGstd4bBmfkvXNliJ-i068LINdWPJ1dOV4'

logging.basicConfig(level=logging.INFO)
from sqlite import Database
import sqlite3

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

db = Database('main.db')

# @dp.message_handler(commands=['start', 'help'])
# async def send_welcome(message: types.Message):
    # name = message.from_user.username
    # try:
    #     db.create_table_users()
    # except:
    #     pass
    # #Foydalanuvchini bazaga qo'shamiz
    # try:
    #     db.add_user(id=message.from_user.id,
    #                 name=message.from_user.full_name,
    #                 email=f"@{name}")
    #     count_user = db.count_users()[0]
    #     mes = f"Bazaga @{name}qo'shildi. Bazada {count_user} odam bor."
    #     await bot.send_message(chat_id=,text=mes)
    # except sqlite3.InternalError:
    #     pass

# @dp.message_handler(user_id=596040733, text="users")
# async def allusers(message: Message):
#     users = db.select_all_users()
#     #await message.answer(users)
#
#     for us in users:
#         await message.answer(f"ID:{us[0]}.Username:{us[2]}")
#
#   try:
#
#    except db.create_table_users()
#
#    await message.reply("Assalomu alekum",reply_markup=Bosh_sahifa)

@dp.message_handler(commands="start")
async def bulochka(message: types.Message):
    await message.answer("Buluchkalar",reply_markup=types_bulochka)

@dp.message_handler()

@dp.callback_query_handler(text="krem")
async def send_krem(call: CallbackQuery):
    await call.message.answer("Qancha olasiz?",reply_markup=raqamlar)

@dp.callback_query_handler(text="Oddiy")
async def send_kremb(call: CallbackQuery):
    await call.message.answer("Qancha olasiz?",reply_markup=raqamlar)

@dp.callback_query_handler(text="Xitoy_sariq")
async def send_kremb(call: CallbackQuery):
    await call.message.answer("Qancha olasiz?",reply_markup=raqamlar)

@dp.callback_query_handler(text="Xitoy_kok")
async def send_kremb(call: CallbackQuery):
    await call.message.answer("Qancha olasiz?",reply_markup=raqamlar)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
