import asyncio
import time
from tel_ctrl import send
from crawl import get_vcount, get_time
import sqlite3
import os

# INITIALIZE DB
db_path = os.getcwd() + '/userdb.db'
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS user(id text, pwd text, chatid text, lastcount int, lasttime int)")
'''
[0] : id
[1] : pwd
[2] : chatid
[3] : lastcount
[4] : lasttime
'''

# UPDATE lastcount for ALL registered users
c.execute("SELECT * FROM user")
table_list = c.fetchall()
for usr in table_list:
    c.execute("UPDATE user SET lastcount = {} WHERE id = '{}'".format(get_vcount(usr[0],usr[1]),usr[0]))
    c.execute("UPDATE user SET lasttime = {} WHERE id = '{}'".format(get_time(usr[0],usr[1]),usr[0]))
    # asyncio.run(send("{}님의 마이픽이북 검수완료 알림 서비스 시작".format(usr[0]),usr[2]))
conn.commit()
    

print("MONITERING STARTED")
# LOOP
while True:
    c.execute("SELECT * FROM user")
    table_list = c.fetchall()
    for usr in table_list:
        new_count = get_vcount(usr[0],usr[1])
        if new_count > usr[3]:
            new_time = get_time(usr[0],usr[1])
            time_added = new_time - usr[4]
            c.execute("UPDATE user SET lastcount = {} WHERE id = '{}'".format(new_count,usr[0]))
            c.execute("UPDATE user SET lasttime = {} WHERE id = '{}'".format(new_time,usr[0]))
            conn.commit()
            asyncio.run(send("""검수가 완료되었습니다
+ {}시간 {}분 {}초""".format(int(time_added/3600),int((time_added%3600)/60),time_added%3600%60),usr[2]))
            print("SENT MSG to {}".format(usr[0]))
    time.sleep(60)
    