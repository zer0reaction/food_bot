import telebot, constants
import db

bot = telebot.TeleBot(token=constants.TOKEN, parse_mode="Markdown")


@bot.message_handler()
def message_handler(message):
    text = message.text
    in_whitelist = message.from_user.id in constants.WHITELIST

    if in_whitelist:
        if text == "/start":
            bot.send_message(message.from_user.id, "*Hello!*")


bot.polling()
