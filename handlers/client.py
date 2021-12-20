from aiogram import types, Dispatcher
from create_bot import dp, bot
from telegram import ParseMode

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    await bot.send_message(-1001716903568, str(message.from_user.id) + ' ' + str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + ' ' + '@' + str(message.from_user.username))
    await message.answer("Здравствуйте, я бот Олег. Чтобы подключиться, нажмите на кнопку :@Moneyplace_storage_Bot.")
    await message.answer("Чтобы попасть в чат складчины : @moneyplaceskladchina")
    await message.answer("")

    
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])