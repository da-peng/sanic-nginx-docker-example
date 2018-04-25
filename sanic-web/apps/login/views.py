#encoding=utf-8
from os import environ
from sanic.views import HTTPMethodView
from sanic.response import text

from apps import  app

class SimpleAsyncView(HTTPMethodView):

  async def get(self, request):


      env_conf = app.config.CUSTOM_CONF
      env = app.config.ENV

      return text('能看到我，说明你成功了，'
                  '\n下面打印一下\'MYAPP_CUSTOM_CONF\'环境变量:{}'
                  '\n以及当前系统环境ENV:{}'.format(env_conf,env))