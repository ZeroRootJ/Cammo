from dbmanager import *
from crawl import *
import time
import asyncio
import telegram
from telegram import ForceReply, Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
import os
import sqlite3
import logging


'''
https://docs.python-telegram-bot.org/en/stable/examples.html
'''


UID, PWD = range(2)

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO,
    datefmt='%m/%d/%Y %I:%M:%S %p',
)

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
    
    
    
"""
Functions for conversationhandler
"""
async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "사용자 등록을 시작합니다.\n"
        "사이트 ID를 입력해주세요")

    return UID


async def uid(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = update.message.text
    context.user_data["UID"] = text
    
    # logging.info("UID: {}".format(text))
    
    await update.message.reply_text("사이트 password를 입력해주세요")

    return PWD


async def pwd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    text = update.message.text
    context.user_data["PWD"] = text
    
    # logging.info("PWD: {}".format(update.message.text))
    # logging.info(context.user_data)
    
    try:
        get_vcount(context.user_data["UID"],context.user_data["PWD"])
    except:
        await update.message.reply_text(
            "LOGIN 실패\n"
            "다시 시도해주세요")
    else:
        execute_db("INSERT INTO user VALUES ('{}', '{}', {}, {}, {})".format(
            context.user_data["UID"],
            context.user_data["PWD"],
            update.message.chat.id,
            get_vcount(context.user_data["UID"],context.user_data["PWD"]),
            get_time(context.user_data["UID"],context.user_data["PWD"])
            ))
        
        await update.message.reply_text(
            "LOGIN 성공!\n"
            "검수 완료 시 메세지가 전송됩니다")
    finally:
        return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    """Cancels and ends the conversation."""
    user = update.message.from_user
    logging.info("User %s canceled the conversation.", user.first_name)
    await update.message.reply_text(
        "Bye! I hope we can talk again some day.", reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END


    
"""Start the bot."""
# Create the Application and pass it your bot's token.
application = Application.builder().token(token).build()

conv_handler = ConversationHandler(
    entry_points=[CommandHandler("login", login)],
    states={
        UID: [MessageHandler(filters.TEXT & ~filters.COMMAND, uid)],
        PWD: [MessageHandler(filters.TEXT & ~filters.COMMAND, pwd)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

application.add_handler(conv_handler)

# on different commands - answer in Telegram
application.add_handler(CommandHandler("check", check_command))
application.add_handler(CommandHandler("record", record_command))



# on non command i.e message - echo the message on Telegram
# application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot until the user presses Ctrl-C
application.run_polling()
