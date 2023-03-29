## Cammo  

### Description
실로암복지관 전자도서제작 사이트(www.mypickebook.org/) 에서 제작한 도서의 검수완료 여부를 주기적으로 확인하여 검수가 완료되었을시 알림을 사용자의 텔레그램으로 전달해주는 서비스입니다.  

### Environment  
Python 3.7.4  
python-telegram-bot 20.0  
sqlite3  
goormIDE (Chrome 서브프로세스 사용금지 정책(*selenium 사용불가)으로 인해 bs4, requests 사용)    

### Usage   
- Requirements  
    Telegram에서 생성된 Telegram Bot 및 TOKEN (.env파일에 추가)  
    유저정보를 포함한 userdb.db  
    
- 서비스 실행  
    nohup python3 loop.py &  
  
- 서비스 종료  
    ps ux  
    kill -9 PID  
  
### DEV log  
23.03.09 1인용 알림 서비스 구현 v1.0  
23.03.11 2인 이상 서비스를 위한 유저 DB 추가 및 관련 함수 변경 v2.0  
23.03.29 DB 관리 함수 업데이트(dbmanager)