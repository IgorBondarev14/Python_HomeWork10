from aiogram.types import *

b1 = KeyboardButton('1')
b2 = KeyboardButton('2')
b3 = KeyboardButton('3')
b4 = KeyboardButton('4')
b5 = KeyboardButton('5')
b6 = KeyboardButton('6')
b7 = KeyboardButton('7')
b8 = KeyboardButton('8')
b9 = KeyboardButton('9')
b0 = KeyboardButton('0')
b_dot = KeyboardButton('.')
b_plus = KeyboardButton('+')
b_minus = KeyboardButton('-')
b_mult = KeyboardButton('*')
b_div = KeyboardButton('/')
b_eq = KeyboardButton('=')

kb = ReplyKeyboardMarkup()
kb.row(b1, b2, b3, b_plus).row(b4, b5, b6, b_minus).row(b7, b8, b9, b_mult).row(b0, b_dot, b_eq, b_div)