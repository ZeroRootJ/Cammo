import requests
import os
import re
from bs4 import BeautifulSoup

def get_vcount(login_id,login_pwd):
    session = requests.session()

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


def get_time(login_id,login_pwd):
    session = requests.session()

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
    time_raw = soup.select_one('#content > div.mypageTop1 > ul > li:nth-child(4) > span').get_text()
    time_split = time_raw.split(' ')
    time_inseconds = 0
    for timestr in time_split:
        if '시간' in timestr:
            time_inseconds += int(re.findall(r'\d+',timestr)[0])*3600
        elif '분' in timestr:
            time_inseconds += int(re.findall(r'\d+',timestr)[0])*60
        elif '초' in timestr:
            time_inseconds += int(re.findall(r'\d+',timestr)[0])

    # time_raw = '00시간 00분 00초' > time_inseconds 000000 (seconds)

    return time_inseconds


def get_record(login_id, login_pwd):
    
    # 파싱할 정보에 접근하기 위해 로그인이 필요한 웹사이트의 경우 로그인 후 로그인 상태를 유지하기 위해 session 이용 
    session = requests.session()

    # 사이트에서 요구하는 로그인에 필요한 정보
    login_info = {
        "login_id" : login_id,
        "login_pwd" : login_pwd
    }

    # 로그인 절차에 header도 같이 넣어줘야 로그인이 가능한 경우도 있음
    headers = {
        "Referer" : "http://www.mypickebook.org/member/login.html",
        "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
    }

    # 로그인을 진행하는 url에 적절한 method(해당 경우 post)로 로그인 정보를 전달
    url_login = "http://www.mypickebook.org/member/login_proc.php"
    response = session.post(url_login,data=login_info,headers=headers)
    response.raise_for_status()
    #print(response.text)

    # 파싱할 데이터가 있는 페이지로 이동 (세션 내에서 이동함으로서 로그인 상태 유지)
    url_mypage = "http://www.mypickebook.org/mypage/book.html"
    response = session.get(url_mypage)
    response.raise_for_status()
    #print(response.text)

    # soup를 이용하여 정보 파싱
    soup = BeautifulSoup(response.text,'html.parser')
    # 파싱할 정보 웹사이트에서 우클릭 > 검사 > 우클릭 > Copy > Copy Selector
    pages = soup.select_one('#content > div.mypageTop1 > ul > li:nth-child(1) > span').get_text()
    count = soup.select_one('#content > div.mypageTop1 > ul > li:nth-child(3) > span').get_text()
    time = soup.select_one('#content > div.mypageTop1 > ul > li:nth-child(4) > span').get_text()
    
    txt = "<<내 봉사기록>>\n제작 완료 페이지: {}\n총 봉사 횟수: {}\n총 봉사 시간: {} ".format(pages,count,time)
    
    return txt