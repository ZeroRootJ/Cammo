import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

def get_vcount():
    session = requests.session()

    load_dotenv()
    login_id = os.environ.get("LOGIN_ID")
    login_pwd = os.environ.get("LOGIN_PWD")
    
    login_info = {
        "login_id" : login_id,
        "login_pwd" : login_pwd
    }

    headers = {
        "Referer" : "http://www.mypickebook.org/member/login.html",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    url_login = "http://www.mypickebook.org/member/login_proc.php"
    response = session.post(url_login,data=login_info,headers=headers)
    response.raise_for_status()
    #print(response.text)

    url_mypage = "http://www.mypickebook.org/mypage/book.html"
    response = session.get(url_mypage)
    response.raise_for_status()
    #print(response.text)


    soup = BeautifulSoup(response.text,'html.parser')
    vcount = soup.select_one('#content > div.mypageTop1 > ul > li:nth-child(3) > span')
    #print(v_count.get_text())

    return int(vcount.get_text())