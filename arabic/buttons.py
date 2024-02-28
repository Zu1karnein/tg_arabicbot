from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from bot import get_random_arabic_letter, ARABIC_ALPHABET, randl


letter_list = []

while len(letter_list) < 5:
    letter = ARABIC_ALPHABET[get_random_arabic_letter()]

    if letter not in letter_list:
        letter_list.append(letter)




async def menu():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Повторить", callback_data="repeat")
    ])

    keyboard.adjust(1)
    return keyboard.as_markup()

async def back():
    keyboard = InlineKeyboardBuilder()


    keyboard.row(*[
        InlineKeyboardButton(text="Назад", callback_data="repeat")
    ])


    return keyboard.as_markup()

async def repeat():
    keyboard = InlineKeyboardBuilder()

    keyboard.row(*[
        InlineKeyboardButton(text="Ручной режим", callback_data="manual"),
        InlineKeyboardButton(text="Выбор варианта", callback_data="get_letter_keyboard")
    ])

    # keyboard.row(*[
    #     InlineKeyboardButton(text="Назад", callback_data="menu")
    # ])


    return keyboard.as_markup()


# async def options():
#     keyboard = InlineKeyboardBuilder()

#     keyboard.row(*[
#         InlineKeyboardButton(text=randl, callback_data="w"),
#         InlineKeyboardButton(text=randl2, callback_data="w2"),
#         InlineKeyboardButton(text=randl3, callback_data="w3"),
#         InlineKeyboardButton(text=randl4, callback_data="w4")
#     ])

#     keyboard.row(*[
#         InlineKeyboardButton(text="Назад", callback_data="repeat")
#     ])
#     return keyboard.as_markup()


async def get_letter_keyboard(letter_list: list):

    keyboard = InlineKeyboardBuilder()

    btns = []

    for index, letter in enumerate(letter_list):
        btns.append(InlineKeyboardButton(text=letter, callback_data=f"w{index}"))

    keyboard.row(*btns)

    return keyboard.as_markup()




# async def manual_menu():
