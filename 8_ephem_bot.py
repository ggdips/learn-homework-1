#!/usr/bin/python3
"""
Домашнее задание №1
Использование библиотек: ephem
* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.
"""
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import date

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    logging.info('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

def talk_to_me(update, context):
    user_text = update.message.text 
    logging.info(user_text)
    update.message.reply_text(user_text)

def where_is_planet(update, context):
    logging.info('Вызван /planet')
    planet = update.message.text.split()[1]
    constellation = ephem.constellation
    if planet == "Mercury":
        constellation  = ephem.constellation(ephem.Mercury(date.today()))
    if planet == "Venus":
        constellation  = ephem.constellation(ephem.Venus(date.today()))
    if planet == "Mars":
        constellation  = ephem.constellation(ephem.Mars(date.today()))
    if planet == "Jupiter":
        constellation  = ephem.constellation(ephem.Jupiter(date.today()))
    if planet == "Saturn":
        constellation  = ephem.constellation(ephem.Saturn(date.today()))
    if planet == "Uranus":
        constellation  = ephem.constellation(ephem.Uranus(date.today()))
    if planet == "Neptune":
        constellation  = ephem.constellation(ephem.Neptune(date.today()))
    update.message.reply_text(f'{planet} in {constellation[1]}')

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", where_is_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()
