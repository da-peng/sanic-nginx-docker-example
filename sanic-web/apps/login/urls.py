#encoding=utf-8


from .views import *
from . import login

login.add_route(SimpleAsyncView.as_view(),'/')