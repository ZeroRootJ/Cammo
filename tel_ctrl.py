import time
import asyncio
import telegram
from dotenv import load_dotenv
import os

'''
async def main():
    bot = telegram.Bot(token)
    async with bot:
        print((await bot.get_updates())[0])

'''

async def send(msg):
    load_dotenv()
    token = os.environ.get("TOKEN")
    chat_id = os.environ.get("CHAT_ID")
    
    bot = telegram.Bot(token)
    async with bot:
        await bot.send_message(text=msg, chat_id=chat_id)


'''
if __name__ == '__main__':
    asyncio.run(main())
'''

'''
while True:
    asyncio.run(send())
    time.sleep(5)
    print("msg sent")
'''    

