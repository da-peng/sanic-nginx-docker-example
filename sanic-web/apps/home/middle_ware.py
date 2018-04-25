#encoding=utf-8
from apps.home import home
from sanic.response import text


# 中间件
@home.middleware
async def print_on_request(request):
    print("I am a spy")

# @home.middleware('request')
# async def halt_request(request):
#     return text('I halted the request')
#
# @home.middleware('response')
# async def halt_response(request, response):
#     return text('I halted the response')
#
