from aiogram import types, Dispatcher, bot
from create_bot import dp

@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
    # await bot.send_message(message.text)
    
    await message.answer("Мы рады что Вы присоединились к нам!!!", message.from_user.id)
    await message.answer("Ссылка на оригинального бота: @Moneyplace_storage_Bot")
    await message.answer("Переходите и пользуйтесь")
    await message.answer("Спасибо")
    
    print(message.text)
    
def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])