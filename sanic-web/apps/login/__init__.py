#encoding=utf-8

from sanic.blueprints import Blueprint

# url前缀，配置为host/
# 初始化蓝本
login = Blueprint('login',url_prefix='/')


__all__ = ('urls','views','middle_ware')

from apps.login import *
