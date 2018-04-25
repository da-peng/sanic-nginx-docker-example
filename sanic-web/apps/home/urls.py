#encoding=utf-8
from . import home
from .views import *



# 路由配置 /home/simple   蓝本uri前缀 + 配置路径
home.add_route(SimpleAsyncView.as_view(),'/simple')