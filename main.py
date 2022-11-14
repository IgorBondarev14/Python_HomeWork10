import logging

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from keyboard import kb
from message_log import mes_log

logging.basicConfig(filename='loger.txt', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s, level=logging.Debug')

bot = Bot(token='токен')
dp = Dispatcher(bot)


@dp.message_handler(commands = ['start'])
async def cmd_start(message: types.Message):
    mes_log(message)
    message_logger = open('message_loger.txt', 'a', encoding='utf-8')
    message_logger.write(f'Бот написал: Привет, {message.from_user.first_name}! Начнём?\n')
    message_logger.close()
    await message.answer(f'Привет, {message.from_user.first_name}!\nНачнём?', reply_markup=kb)

calc_str = ''

@dp.message_handler(content_types = ['text'])
async def calc(message: types.Message): 
    mes_log(message)   
    global calc_str
    if message.text != '=':
        if message.text == '+' or message.text == '-' or message.text == '*' or message.text == '/':
            calc_str = calc_str + ';'+ ''.join(message.text) + ';'
        elif message.text.isdigit() or message.text.count('.') == 1:
            calc_str = calc_str + ''.join(message.text)
    else:
        res_list = calc_str.split(';')
        calc_str = calc_str[len(calc_str):]
        if res_list[1] == '+':
            result = float(res_list[0]) + float(res_list[2])
            message_logger = open('message_loger.txt', 'a', encoding='utf-8')
            message_logger.write(f'Бот написал: {res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}\n')
            message_logger.close()
            await message.answer(f'{res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}')
        elif res_list[1] == '-':
            result = float(res_list[0]) - float(res_list[2])
            message_logger = open('message_loger.txt', 'a', encoding='utf-8')
            message_logger.write(f'Бот написал: {res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}\n')
            message_logger.close()
            await message.answer(f'{res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}')
        elif res_list[1] == '*':
            result = float(res_list[0]) * float(res_list[2])
            message_logger = open('message_loger.txt', 'a', encoding='utf-8')
            message_logger.write(f'Бот написал: {res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}\n')
            message_logger.close()
            await message.answer(f'{res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}')
        elif res_list[1] == '/':
            result = float(res_list[0]) / float(res_list[2])
            message_logger = open('message_loger.txt', 'a', encoding='utf-8')
            message_logger.write(f'Бот написал: {res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}\n')
            message_logger.close()
            await message.answer(f'{res_list[0]} {res_list[1]} {res_list[2]} = {round(result, 10)}')
        else:
            await message.answer(f'Что-то пошло не так!')


executor.start_polling(dp, skip_updates=True)

