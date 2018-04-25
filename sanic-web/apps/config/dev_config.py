#encoding=utf-8
# dev_config
# #!/usr/bin/env python
from .config import Config

# dev环境配置
class DevConfig(Config):
    """
    Dev config for demo02
    """
    # Application config
    DEBUG = True
