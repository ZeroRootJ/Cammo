import sqlite3
import os
from crawl import get_vcount

# Execute on DB
def execute_db(SQLCMD):
    db_path = os.getcwd() + '/userdb.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(SQLCMD)
    conn.commit()
    conn.close()
    
    
# Check DB
def check_db():
    db_path = os.getcwd() + '/userdb.db'
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT * FROM user")
    table_list = c.fetchall()
    for usr in table_list:
        print(usr)
    conn.close()
    

# Delete User
# execute_db("DELETE FROM user WHERE id='birdonmars'")

# Insert USER
# execute_db("INSERT INTO user VALUES ('id', 'pwd', 'telegram_chatid', VolunteerNumber, Time)")

# ADD Coloumn
# execute_db('ALTER TABLE user ADD lasttime INT')

check_db()