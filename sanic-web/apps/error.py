#encoding=utf-8

from sanic.response import text
from sanic.exceptions import NotFound
from . import app

# 仅home蓝本的 NotFound错误处理
@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the  page: {}".format(request.url))