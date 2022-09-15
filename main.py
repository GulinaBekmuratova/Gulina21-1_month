from aiogram import types
from aiogram.utils import executor
from config import bot,dp
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from handlers import admin,callback,client,extra


admin.register_handlers_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
extra.register_handlers_extra(dp)








if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)







#

#
#
#
#
#
#
#
#
#
#
#
#
#
#
# from aiogram import types
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.utils import executor
# from config import bot, dp
# import logging
#
#
# @dp.message_handler(commands=['start', 'help'])
# async def command_start(message: types.Message):
#     await message.answer(f"Салалекум {message.from_user.full_name}")
#     await message.reply(f"Привет босс {message.from_user.first_name}!")
#
#
# @dp.message_handler(commands=['quiz'])
# async def quiz_1(message: types.Message):
#     markup = InlineKeyboardMarkup()
#     button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
#     markup.add(button_call_1)
#
#     question = "Сколько живут обезьяны?"
#     answers = [
#         "15 лет",
#         "11 лет",
#         "5 лет",
#         "20 лет",
#         "100 лет",
#     ]
#     await bot.send_poll(
#         chat_id=message.chat.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=3,
#         explanation="Если ты не знаешь, то ты обезьяна!",
#         open_period=10,
#         reply_markup=markup
#     )
#
#
# @dp.callback_query_handler(lambda call: call.data == "button_call_1")
# async def quiz_2(call: types.CallbackQuery):
#     markup = InlineKeyboardMarkup()
#     button_call_2 = InlineKeyboardButton("NEXT", callback_data="button_call_2")
#     markup.add(button_call_2)
#
#     question = "By whom invented Python??"
#     answers = [
#         "Harry Potter",
#         "Putin",
#         "Guido Van Rossum",
#         "Voldemort",
#         "Griffin",
#         "Linus Torvalds",
#     ]
#     await bot.send_poll(
#         chat_id=call.message.chat.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=2,
#         explanation="ИЗЗИ!",
#         open_period=10,
#         reply_markup=markup
#     )
#
#
# @dp.callback_query_handler(lambda call: call.data == "button_call_2")
# async def quiz_3(call: types.CallbackQuery):
#     question = "Solve:"
#     answers = [
#         '4',
#         '8',
#         '4, 6',
#         '2, 4',
#         '5',
#     ]
#     photo = open('media/problem1.jpg', 'rb')
#     await bot.send_photo(call.from_user.id, photo)
#     await bot.send_poll(
#         chat_id=call.message.chat.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type='quiz',
#         correct_option_id=3,
#         explanation="ИЗЗИ!",
#         open_period=10,
#     )
#
#
# @dp.message_handler(content_types=['text', 'photo'])
# async def echo(message: types.Message):
#     if message.text == 'bot':
#         await message.answer("Human")
#     await bot.send_message(message.from_user.id, message.text)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO)
#     executor.start_polling(dp, skip_updates=True)