from aiogram import types


def mes_log(message: types.Message):
    message_logger = open('message_loger.txt', 'a', encoding='utf-8')
    message_logger.write(f'{message.from_user.first_name} {message.from_user.last_name}, \
        {message.from_user.id}, {message.text}, {message.date}\n')
    message_logger.close()
    
