from auth import token
import telebot

def telega_bot_error(text_error):
    bot = telebot.TeleBot(token)
    bot.send_message(tg_id, f'Ошибочка вышла: \n {text_error}')

def telega_bot_result(text_result):
    bot = telebot.TeleBot(token)
    bot.send_message(tg_id, f'{text_result}')