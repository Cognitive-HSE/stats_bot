import telebot
import psycopg2

bot = telebot.TeleBot('7727243987:AAEn7_ubkN5ueBQWK_rjmmikqIBAN9JqwK4')

@bot.message_handler(commands=["stats"])
def start(m, res=False):
    reply = ''

    with psycopg2.connect(user="python_bot",
                            password="python_bot",
                            host="79.137.204.140",
                            port="5000",
                            database="cognitive") as conn:
        with conn.cursor() as cursor:
            cursor.execute('select cognitive.f$sys__stats()')
            reply = cursor.fetchone()[0]

    bot.send_message(m.chat.id, reply)

bot.polling(none_stop=True, interval=0)