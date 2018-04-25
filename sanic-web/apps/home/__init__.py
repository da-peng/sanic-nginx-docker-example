#encoding=utf-8
from sanic import  Blueprint

# print(__name__)# apps.home

# 初始化模板
home = Blueprint('home',url_prefix='/home')

__all__ = ['urls','views']
# import model
from apps.home import *
# import package  __init__.py  既可以指定模块，还可以指定变量 模块名 变量名

