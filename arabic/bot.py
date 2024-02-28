import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.types.bot_command import BotCommand
from aiogram.types import FSInputFile, Message
from aiogram.filters import Command
import random

from config import TOKEN
from alphabet import ARABIC_ALPHABET
from buttons import *


bot_commands = [
    BotCommand(command="/start", description="Menu"),
    BotCommand(command="/help", description="Раздел помощь"),
]


# logging start
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

# polling start
async def main():
    await bot.set_my_commands(commands=bot_commands)
    await bot.send_message(chat_id="1905209181", text="Bot started\n\n/start")
    await dp.start_polling(bot)



# start command and button
@dp.message(Command('start'))
@dp.callback_query(F.data == 'start')
async def start(obj: types.Message | types.CallbackQuery):
    await obj.answer('Ассаламу алайкум варохьматуллох1\nЭтот бот позволит вам повторить изученный вами арабский алфавит', reply_markup=await menu())

# # help command and button
# @dp.message(Command('help'))
# @dp.callback_query(F.data == 'help')
# async def help(obj: types.Message | types.CallbackQuery):

#     if isinstance(obj, types.Message):
#         await obj.answer('Это простой бот для изучения Inline кнопок.\nЧтобы перейти к выбору раздела пропишите команду "/start", или выберите эту команду в Меню слева.')
#     else:
#         await obj.message.edit_text('Это простой бот для изучения Inline кнопок.\nЧтобы перейти к выбору раздела:\n* Пропишите команду "/start"\n* Нажмите кнопку снизу "Назад"\n* Выберите эту команду в Меню слева.', reply_markup=await help_command()) # type: ignore

# случайная буква из алфавита
def get_random_arabic_letter():
    return random.choice(list(ARABIC_ALPHABET.keys()))

randl = get_random_arabic_letter()


@dp.callback_query(F.data == 'repeat')
async def data_repeat(call: types.CallbackQuery):
    await call.answer()
    if call.message:
       await call.message.edit_text('Выберите подраздел:', reply_markup=await repeat())
    #    await msg.delete()


@dp.callback_query(F.data == 'get_letter_keyboard')
async def manual_mode(call: types.CallbackQuery):
    await call.answer()
    if call.message:
        await call.message.edit_text(f'Как называется эта буква: {randl}?', reply_markup=await back())


@dp.callback_query(F.data == 'options')
async def options_mode(call: types.CallbackQuery):
    await call.answer()
    if call.message:          
        await call.message.edit_text(f'Как называется эта буква: {randl}?\nВыберите вариант из списка:', reply_markup=await get_letter_keyboard())





if __name__ == '__main__':
    asyncio.run(main())