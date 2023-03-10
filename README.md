## Cammo  

### Description
실로암복지관 전자도서제작 사이트(www.mypickebook.org/) 에서 제작한 도서의 검수완료 여부를 주기적으로 확인하여 검수가 완료되었을시 알림을 사용자의 텔레그램으로 전달해주는 서비스입니다.  

### Environment  
Python 3.7.4
python-telegram-bot 20.0
goormIDE (Chrome 서브프로세스 사용금지 정책(*selenium 사용불가)으로 인해 bs4, requests 사용)  

### Usage

- requirements  
  {USER_ID=사이트 유저 아이디, USER_PWD=사이트 유저 패스워드, TOKEN=텔레그램 봇 토큰, CHAT_ID=사용자의 텔레그램 챗 아이디}를 포함한 .env 파일
  
- 서비스 실행  
  nohup python3 loop.py &

- 서비스 종료  
  ps ux  
  kill -9 PID
