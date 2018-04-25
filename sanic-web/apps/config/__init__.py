#encoding=utf-8
#!/usr/bin/env python
import os
from apps import app

def load_config():

    """
    Load a config class
    """
    # mode = os.environ.get('MODE', 'DEV')
    tmp = app.config.ENV
    # 函数生成器，可以替代Java中的三目运算
    env = tmp if tmp!=None  else 'DEV'
    try:
        if env == 'PRO':
            from .pro_config import ProConfig
            return ProConfig
        elif env == 'DEV':
            from .dev_config import DevConfig
            return DevConfig
        else: # 默认使用Dev
            from .dev_config import DevConfig
            return DevConfig

    except ImportError:
        from .config import Config
        return Config

CONFIG = load_config()

