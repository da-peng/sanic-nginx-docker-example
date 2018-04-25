#encoding=utf-8

from sanic.views import HTTPMethodView
from sanic.response import text

# 使用class-base 完成view的控制，http相关业务处理，View controller

class SimpleAsyncView(HTTPMethodView):

  async def get(self, request):

      return text('I am async get method')

