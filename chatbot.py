import telebot

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with the actual token you obtained from BotFather
BOT_TOKEN = "7465884972:AAGghEJ9Vi2uYgTlZfVEGs7vspxXmPweR2E"

bot = telebot.TeleBot(BOT_TOKEN)

# Define a dictionary to store chatbot responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "how are you": "I'm doing well, thank you for asking!",
    "what is your name": "I am a simple Telegram bot.",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand. Please try again."
}

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    # Get the message text
    text = message.text.lower()

    # Check if the message is in the responses dictionary
    if text in responses:
        bot.reply_to(message, responses[text])
    else:
        bot.reply_to(message, responses["default"])

bot.infinity_polling()