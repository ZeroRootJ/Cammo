import time
import asyncio
import telegram
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
from dotenv import load_dotenv
from crawl import get_record
import os
import sqlite3

'''
https://docs.python-telegram-bot.org/en/stable/examples.html
'''

load_dotenv()
token = os.environ.get("TOKEN")

async def check_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /check 이라는 커맨드가 채팅창에 입력되었을 때 챗봇시스템의 가동여부를 확인하여 메세지 전송
    """
    await update.message.reply_text("정상 작동 중입니다.")

    
async def record_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    /record
    """
    chatid = update.message.chat.id
    
    db_path = os.getcwd() + '/userdb.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM user WHERE chatid = '{}'".format(chatid))
    usr = c.fetchall()[0]
    
    await update.message.reply_text(get_record(usr[0],usr[1]))

    
    
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

    
"""Start the bot."""
# Create the Application and pass it your bot's token.
application = Application.builder().token(token).build()

# on different commands - answer in Telegram
application.add_handler(CommandHandler("check", check_command))
application.add_handler(CommandHandler("record", record_command))


# on non command i.e message - echo the message on Telegram
# application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot until the user presses Ctrl-C
application.run_polling()
