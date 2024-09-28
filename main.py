import telebot, constants, db
from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup

bot = telebot.TeleBot(token=constants.TOKEN, parse_mode="Markdown")


states = (
    "greeting",
    "viewing_list",
    "adding_items_to_list"
)


def greeting(message):
    print("Greeting user {}".format(message.from_user.id))

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
    db.update_user_state(message.from_user.id, states[0]) # greeting


def view_list(message):
    print("User {} is viewing list".format(message.from_user.id))
    text = "Test"

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [
        InlineKeyboardButton(text="Back")
    ]

    for button in buttons: markup.add(button)

    bot.send_message(message.chat.id, text, reply_markup=markup)
    db.update_user_state(message.from_user.id, states[1]) # viewing_list


def add_items_to_list(message):
    print("User {} is adding items to list".format(message.from_user.id))

    text = "Test"

    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    buttons = [
        InlineKeyboardButton(text="Back")
    ]

    for button in buttons: markup.add(button)

    bot.send_message(message.chat.id, text, reply_markup=markup)
    db.update_user_state(message.from_user.id, states[2]) # adding_items_to_list


@bot.message_handler()
def message_handler(message):
    print("Handling message")

    state = db.get_user_state(message.from_user.id)
    text = message.text
    in_whitelist = message.from_user.id in constants.WHITELIST

    if in_whitelist:
        # greeting
        if (text == "/start" and state == states[0]) or \
           (text == "/start" and state == None) or \
           (text == "Back" and (state == states[1] or state == states[2])): 
            greeting(message)

        elif text == "View list" and state == states[0]: # greeting
            view_list(message)

        elif text == "Add items to list" and state == states[0]: # greeting
            add_items_to_list(message)


bot.polling()
