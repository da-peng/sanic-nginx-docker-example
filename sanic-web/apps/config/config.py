# encoding=utf-8
import os


# 已Object的形式设置公共配置

class Config(object):

    # db默认配置
    DB_HOST = 'localhost',
    DB_NAME = 'appdb',
    DB_USER = 'appuser',
    # ENV = None,
    
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
