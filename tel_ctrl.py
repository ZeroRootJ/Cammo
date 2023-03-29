import time
import asyncio
import telegram
from dotenv import load_dotenv
import os


async def fetch():
    load_dotenv()
    token = os.environ.get("TOKEN")
    bot = telegram.Bot(token)
    async with bot:
        updates = await bot.get_updates()
    for u in updates:
        print(u.message.chat.id)
        print(u.message.chat.first_name)
        print(u.message.chat.username)
        print(u.message.text)


async def send(msg, chat_id):
    load_dotenv()
    token = os.environ.get("TOKEN")    
    bot = telegram.Bot(token)
    async with bot:
        await bot.send_message(text=msg, chat_id=chat_id)


if __name__ == '__main__':
    asyncio.run(fetch())


'''
while True:
    asyncio.run(send())
    time.sleep(5)
    print("msg sent")
'''    

