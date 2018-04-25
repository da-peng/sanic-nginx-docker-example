#encoding=utf-8

# dev_config
# #!/usr/bin/env python
from .config import Config

# 生产环境配置
class ProConfig(Config):
    """
    Dev config for demo02
    """
    # Application config
    DEBUG = False