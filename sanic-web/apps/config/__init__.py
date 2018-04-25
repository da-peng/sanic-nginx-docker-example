#encoding=utf-8
#!/usr/bin/env python
import os
from apps import app

def load_config():

    """
    Load a config class
    """
    env = os.environ.get('ENV', 'DEV')
    # env = app.config.ENV # 不能使用这句，环境变量生命周期还没回来
    # 函数生成器，可以替代Java中的三目运算
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

