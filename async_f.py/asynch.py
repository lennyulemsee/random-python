#!/usr/bin/python3

import asyncio

async def my_coroutine():
    print("start")
    await asyncio.sleep(4) # Asynchronous sleep for 4 secs
    print("End")

asyncio.run(my_coroutine())
