# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 00:48:22 2022

@author: shinbum
"""

import time

start = time.time()
def sync_fnc():
    for i in range(10):
        time.sleep(0.5)
        print(i)

sync_fnc()
sync_fnc()
sync_fnc()

end = time.time()
print(end - start)

# --------------------------------------------

import asyncio
import time

start = time.time()
async def myFnc():
    for i in range(10):
        await asyncio.sleep(0.5) # 이벤트루프를 블락하지 않음
        print(i)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather( myFnc(), myFnc(), myFnc()))
loop.close()
end = time.time()
print(end - start)

