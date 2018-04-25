#encoding=utf-8
from sanic import Sanic

# 环境变量配置测试，必须在app初始化/也就是就是启动前配置，
# 启动后，配置的环境变量需要重新重启服务

from os import environ

environ["MYAPP_CUSTOM_CONF"] = "42"
environ["MYAPP_DEBUG"] = 'True'
environ["MYAPP_ENV"] = 'DEV'

# 初始化app,初始化的时候将配置一起配了
app = Sanic(__name__,load_env='MYAPP_')

from apps.config import CONFIG
# 以Object的形式 设置 配置包含（公共/默认配置，环境配置）
app.config.from_object(CONFIG)
# 估计要注册蓝本前进行环境配置


# 从系统环境变量拿配置，如DB配置，全部以MYAPP_开头

# 或者设置 SANIC_PREFIX = "SANIC_" 来设置环境变量前缀名，
# 还没有试过，看别人有这么写过

# print(__name__)

# import * 包含的模块，变量；不包含在内的 import package时不导入
__all__ = ['urls','tasks','models','middle_ware','error']
# all必须放在 from apps import * 前面
from apps import *
