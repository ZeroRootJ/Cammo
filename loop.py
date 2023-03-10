import asyncio
import time
from tel_ctrl import send
from crawl import get_vcount


v = get_vcount()
while True:
    v_now = get_vcount()
    if v_now > v:
        v = v_now
        asyncio.run(send("검수가 완료되었습니다"))
        # print(f'msg sent [{v}]')
    time.sleep(10)
    
# nohup python3 /workspace/230307/loop.py &
# ps ux
# kill -9 PID