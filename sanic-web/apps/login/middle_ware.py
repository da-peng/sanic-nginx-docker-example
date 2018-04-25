#encoding=utf-8
from apps.login import login
from sanic.response import text



# 监听
@login.listener('before_server_start')
async def setup_connection(app, loop):
    print('server start')

@login.listener('after_server_stop')
async def close_connection(app, loop):
    print('server close')