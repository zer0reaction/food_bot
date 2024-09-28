import telebot, constants, db
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot(token=constants.TOKEN, parse_mode="Markdown")


# Possible states:
# greeting


def greeting(message):
    user_exists = db.check_user_exists(message.from_user.id)
    text = str()

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [
        InlineKeyboardButton(text="View list"),
        InlineKeyboardButton(text="Add items to list")
    ]

    for button in buttons: markup.add(button)

    if user_exists:
        text = "Welcome back!\nChoose an acion:"
    else:
        text = "Hello and welcome to Food Bot!\nChoose an action:"

    bot.send_message(message.chat.id, text, reply_markup=markup)
    db.update_user_state(message.from_user.id, "greeting")


@bot.message_handler()
def message_handler(message):
    text = message.text
    in_whitelist = message.from_user.id in constants.WHITELIST

    if in_whitelist:
        if text == "/start":
            greeting(message)


bot.polling()
