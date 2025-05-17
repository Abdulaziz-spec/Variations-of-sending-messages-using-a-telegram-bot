# pip install pyTelegramBotApi
import logging

from telebot import TeleBot
from telebot.types import Message

TOKEN = '7596663809:AAE2gncKENJH7zf3LahlZoo2T2epPmU1Pyg'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id  # ИСпользоватеь если нужно получть id пользователь из Тг канала
    username = message.from_user.username
    bot.reply_to(message, f'Привет {username} я твой Бот Для Знакомств')
    bot.send_message(chat_id, 'Давай Найдём тебе Пару мой сладенький')
    bot.send_message(chat_id, 'С кем ты хочешь познакомиться? Девочка👧,Девушка👩‍🎓,Женщина💃')


@bot.message_handler(content_types=['text', 'photo', 'voice'])
def answer_text(message: Message):
    chat_id = message.chat.id

    if message.content_type == 'text':
        text = message.text.lower()
        if text == 'девушка':
            try:
                with open('girlfriend.jpg', 'rb') as photo:
                    bot.send_photo(chat_id, photo, caption='Вот тебе красивая девушка 💁‍♀️')
            except Exception as e:
                bot.send_message(chat_id, f'Ошибка при отправке фото девушки: {e}')

        elif text == 'женщина':
            try:
                with open('woman.jpg', 'rb') as photo:
                    bot.send_photo(chat_id, photo, caption='Вот тебе красивая женщина 👩')
            except Exception as e:
                bot.send_message(chat_id, f'Ошибка при отправке фото женщины: {e}')

        elif text == 'девочка':
            try:
                with open('girl.jpg', 'rb') as photo:
                    with open('svastika.jpg', 'rb') as photo1:
                        bot.send_photo(chat_id, photo, caption='Ага попался детолюб Лови 卐')
                        bot.send_photo(chat_id, photo1, caption='Крестик интересный детолюб')
                        bot.send_message(chat_id,
                                         f'А тут твоя инфа детолюб Твой Id {message.chat.id}, Твой ник{message.from_user.first_name} твой юзер {message.from_user.username} твой Фамилия {message.from_user.last_name},{message.chat.bio}')
            except Exception as e:
                bot.send_message(chat_id, f'Ошибка при отправке фото Гитлера: {e}')
        else:
            bot.send_message(chat_id, 'Я не знаю такого слова 🙃')

    elif message.content_type == 'voice':
        user_voice = message.voice.file_id
        bot.send_voice(chat_id, user_voice)

    elif message.content_type == 'photo':
        user_photo = message.photo[-1].file_id
        bot.send_photo(chat_id, user_photo, caption='Это ты на фото? 😄')


# Запуск бота

bot.polling(logger_level=logging.INFO)
bot.polling(none_stop=True)
