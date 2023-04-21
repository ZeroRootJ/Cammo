## Cammo  

### Description
실로암복지관 전자도서제작 사이트(www.mypickebook.org/) 에서 제작한 도서의 검수완료 여부를 주기적으로 확인하여 검수가 완료되었을시 알림을 사용자의 텔레그램으로 전달해주는 서비스입니다.  
추가적으로 챗봇 명령어를 통해 내 봉사현황을 확인 할 수 있습니다.

### USAGE  
자동으로 검수완료 여부를 확인하여 작업한 책의 검수가 완료되었을시 '검수가 완료되었습니다. +00시간 00분 00초' 메세지를 채팅창에 전송  
    
채팅창에 사용가능한 명령어  
    /check : 봇이 정상작동중인지 확인  
    /record :  나의 봉사기록 확인 (제작한 페이지 수 / 봉사횟수 / 봉사시간)  
    /login : 사용자를 서비스 데이터베이스에 추가  


### Environment  
Python 3.7.4  
python-telegram-bot 20.0  
sqlite3  
goormIDE (Chrome 서브프로세스 사용금지 정책(*selenium 사용불가)으로 인해 bs4, requests 사용)    

### MEMO   
- Requirements  
    Telegram에서 생성된 Telegram Bot 및 TOKEN (.env파일에 추가)  
    유저정보를 포함한 userdb.db  
    
- 서비스 실행  
    nohup python3 loop.py &  
    nohup python3 chathandler.py &  
  
- 서비스 종료  
    ps ux  
    kill -9 PID  
  
### DEV log  
23.03.09 1인용 알림 서비스 구현 v1.0  
23.03.11 2인 이상 서비스를 위한 유저 DB 추가 및 관련 함수 변경 v2.0  
23.03.29 DB 관리 함수 업데이트(dbmanager)  
23.04.16 챗봇 명령어 추가(/check,/record)  
23.04.20 검수 완료 알림과 함께 인증된(추가된) 시간까지 추가 전송  
23.04.21 시간 표시 관련 Bug Fix  
23.04.21 새로운 사용자를 데이터베이스에 추가하는 작업 자동화 (사용자가 채팅창에서 직접 할 수 있도록 기능 제작)  