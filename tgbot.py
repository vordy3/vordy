import telebot

from pyowm import OWM
from pyowm.utils.config import get_default_config
bot = telebot.TeleBot("5519915592:AAEgFiOHXbxRsdzcNqW9RZ-Vr0AmpIQfdIs")

@bot.message_handler(commands=['start'])
def start(message):

    sticker=open('ben.webp','rb')
    bot.send_sticker(message.chat.id,sticker)
    mess=f'<b>Привет! {message.from_user.first_name} {message.from_user.last_name}\n <b>Я-БОТ-ПОГОДА\n </b></b>'
    bot.send_message(message.chat.id,mess,parse_mode='html')
    bot.send_message(message.chat.id,'Чтобы узнать погоду напишите в чат название города')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '/start - запуск бота\n/help - команды бота\nЧтобы узнать погоду напишите в чат название города')

@bot.message_handler(content_types=['text'])
def test(message):
    try:

        place = message.text

        config_dict = get_default_config()
        config_dict['language'] = 'ru'
        owm = OWM('24a40c036edd48a905702ca3a75eed46', config_dict)
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather

        t = w.temperature("celsius")
        t1 = t['temp']
        t2 = t['feels_like']
        t3 = t['temp_max']
        t4 = t['temp_min']
        bot.send_message(message.chat.id, "В городе " +str(place)+ " " +str(t1)+ "°C"+'\n'+
        "Максимальная температура " + str(t3) + " °C" +"\n"+
        "Минимальная температура " + str(t4) + " °C" + "\n"+
        "Ощущается как " + str(t2) + " °C" + "\n")
    except:
        bot.send_message(message.chat.id,"Такой город не найден!")

bot.polling(none_stop=True)