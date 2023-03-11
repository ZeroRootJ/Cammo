import asyncio
import time
from tel_ctrl import send
from crawl import get_vcount
import sqlite3
import os

# INITIALIZE DB
db_path = os.getcwd() + '/userdb.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(id text, pwd text, chatid text, lastcount int)")
'''
[0] : id
[1] : pwd
[2] : chatid
[3] : lastcount
'''

# UPDATE lastcount for ALL registered users
c.execute("SELECT * FROM user")
table_list = c.fetchall()
for usr in table_list:
    c.execute("UPDATE user SET lastcount = {} WHERE id = '{}'".format(get_vcount(usr[0],usr[1]),usr[0]))
    asyncio.run(send("{}님의 마이픽이북 검수완료 알림 서비스 시작".format(usr[0]),usr[2]))
conn.commit()
    
# LOOP
while True:
    c.execute("SELECT * FROM user")
    table_list = c.fetchall()
    for usr in table_list:
        new_count = get_vcount(usr[0],usr[1])
        if new_count > usr[3]:
            c.execute("UPDATE user SET lastcount = {} WHERE id = '{}'".format(new_count,usr[0]))
            conn.commit()
            asyncio.run(send("검수가 완료되었습니다",usr[2]))
    time.sleep(60)
    