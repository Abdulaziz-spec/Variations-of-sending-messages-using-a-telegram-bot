# pip install pyTelegramBotApi
import logging

from telebot import TeleBot
from telebot.types import Message

TOKEN = 'YOUR_TOKEN'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    user_id = message.from_user.id  # ИСпользоватеь если нужно получть id пользователь из Тг канала
    username = message.from_user.username
    bot.reply_to(message, f'Привет {username} я твой Бот Для отправки любого формата файлов напиши например text или '
                          f'напиши голосвой или отправь фото')


@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'venue', 'venue', 'animation'])
def answer_text(message: Message):
    chat_id = message.chat.id

    if message.text:
        user_text = message.text
        bot.send_message(chat_id, f"Сам ты {user_text}")

    elif message.content_type == 'audio':
        user_audio = message.audio.file_id
        bot.send_audio(chat_id, user_audio)

    elif message.content_type == 'document':
        user_document = message.document.file_id
        bot.send_document(chat_id, user_document)

    elif message.content_type == 'photo':
        user_photo = message.photo[-1].file_id
        bot.send_photo(chat_id, user_photo, caption='Это ты на фото? 😄')

    elif message.content_type == 'sticker':
        user_sticker = message.sticker.file_id
        bot.send_sticker(chat_id, user_sticker)
        bot.send_message(chat_id, f'Это ты 👆')

    elif message.content_type == 'video':
        user_video = message.video.file_id
        bot.send_video(chat_id, user_video, caption='это ти)')

    elif message.content_type == 'video_note':
        user_video_note = message.video_note.file_id
        bot.send_video_note(chat_id, user_video_note)

    elif message.content_type == 'voice':
        user_voice = message.voice.file_id
        bot.send_voice(chat_id, user_voice)

    elif message.content_type == 'location':
        user_location = message.location
        bot.send_location(chat_id, latitude=user_location.latitude, longitude=user_location.longitude)

    elif message.content_type == 'contact':
        user_contact = message.contact
        bot.send_contact(chat_id, phone_number=user_contact.phone_number, first_name=user_contact.first_name,
                         last_name=user_contact.last_name if user_contact.last_name else '')
        bot.send_message(chat_id,text='Спасибо за контакты Точно не передам мошейнику')

    elif message.content_type == 'venue':
        user_venue = message.venue
        bot.send_venue(chat_id, latitude=user_venue.location.latitude, longitude=user_venue.location.longitude,
                       title=user_venue.title, address=user_venue.address)
    elif message.content_type == 'animation':
        user_animation = message.animation.file_id
        bot.send_animation(chat_id, user_animation)


bot.polling(logger_level=logging.INFO)
bot.polling(none_stop=True)
