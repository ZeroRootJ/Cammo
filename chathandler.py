import time
import asyncio
import telegram
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
import os

'''
CF
https://docs.python-telegram-bot.org/en/stable/examples.html
'''

load_dotenv()
token = os.environ.get("TOKEN")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

"""Start the bot."""
# Create the Application and pass it your bot's token.
application = Application.builder().token(token).build()

# on different commands - answer in Telegram
application.add_handler(CommandHandler("help", help_command))

# on non command i.e message - echo the message on Telegram
application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot until the user presses Ctrl-C
application.run_polling()
