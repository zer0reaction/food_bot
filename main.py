import telebot, constants, db

bot = telebot.TeleBot(token=constants.TOKEN, parse_mode="Markdown")


def greeting(message):
    user_exists = db.check_user_exists(message.from_user.id)

    if user_exists:
        bot.send_message(message.chat.id, "Welcome back! Choose an action:")
    else:
        bot.send_message(message.chat.id, "Hello! Choose an action:")


@bot.message_handler()
def message_handler(message):
    text = message.text
    in_whitelist = message.from_user.id in constants.WHITELIST

    if in_whitelist:
        if text == "/start":
            greeting(message)


bot.polling()
