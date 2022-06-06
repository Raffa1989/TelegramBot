import telebot
from requests import get

bot = telebot.TeleBot("TOKEN")

# приветственное сообщение
@bot.message_handler(commands=['start', ])
def repeat(message: telebot.types.Message):
    print(message.text)            #необязательно прописывать принты
    bot.reply_to(message, f'Тебе здесь не рады, {message.chat.username}')

# ответ на запрос помощи
@bot.message_handler(commands=['help', ])
def repeat(message: telebot.types.Message):
    print(message.text)
    bot.reply_to(message, f'Ничем помочь не могу, у меня лапки')

# Обрабатываются текстовые сообщения
@bot.message_handler(content_types=['text', ])
def u(message: telebot.types.Message):
    print(message.text)
    if message.text == 'Привет':
       # bot.send_message(message.chat.id, 'Просто здравствуй, просто "Как дела?"')
       bot.send_photo(message.chat.id, get(('https://memepedia.ru/wp-content/uploads/2020/02/prosto-zdravstvuj-prosto-kak-dela-1.png')).content)

    elif message.text == 'Как дела?':
       # bot.send_message(message.chat.id, "До того, как ты спросил, было все хорошо")
        bot.send_photo(message.chat.id, get(('https://cs13.pikabu.ru/post_img/big/2019/01/23/8/1548245495111526608.jpg')).content)

    elif message.text == 'Пока':
       # bot.send_message(message.chat.id, "До того, как ты спросил, было все хорошо")
        bot.send_photo(message.chat.id, get(('https://lh3.googleusercontent.com/proxy/0lTXujNvdOvNJbHZLnMPQG4xo7Ph3ja3m9AuJ3UZx-_hNf4x2pIY7mM_ayF1ruYSB1niwVDisDikIE3ckEp3eHikxd0iUv_F')).content)

    else:
        bot.send_message(message.chat.id, "Я еще маленький, только учусь. На это я еще не умею реагировать")

# Обрабатываются все картинки
@bot.message_handler(content_types=['photo', ])
def i(message: telebot.types.Message):
    print(message.photo)
    bot.send_message(message.chat.id, "Класс!")

# Обрабатываются все голосовые сообщения
@bot.message_handler(content_types=['voice', ])
def u(message: telebot.types.Message):
    print(message.voice)
    bot.send_message(message.chat.id, "Долой ваши голосовые сообщения!")

# Обрабатываются все документы
@bot.message_handler(content_types=['document', ])
def u(message: telebot.types.Message):
    print(message.document)

# Обрабатываются стикеры
@bot.message_handler(content_types=['sticker', ])
def u(message: telebot.types.Message):
    print(message.sticker)
    bot.send_message(message.chat.id, "Ееее, я тоже научусь скоро отвечать стикерами!")

# Обрабатываются все аудиозаписи
@bot.message_handler(content_types=['audio', ])
def u(message: telebot.types.Message):
    print(message.audio)
    bot.send_message(message.chat.id, "Больше басов!")

# Обрабатываются все видеозаписи
@bot.message_handler(content_types=['video', ])
def u(message: telebot.types.Message):
    print(message.video)

# Обрабатываются присланные контакты
@bot.message_handler(content_types=['contact', ])
def u(message: telebot.types.Message):
    print(message.contact)
    bot.send_message(message.chat.id, "Контакт передан в ФСБ")

# Обрабатывается геолокация
@bot.message_handler(content_types=['location', ])
def u(message: telebot.types.Message):
    print(message.location)
    bot.send_message(message.chat.id, "Мы в жопе")

bot.polling(none_stop=True)
