#encoding=utf-8
import asyncio

from apps import app

# 定时任务

async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5) #称为协程（coroutine）
    #  http://www.zhimengzhe.com/bianchengjiaocheng/qitabiancheng/254238.html
    print('Server successfully started!')

# app.add_task(notify_server_started_after_five_seconds())