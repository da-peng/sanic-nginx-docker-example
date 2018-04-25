#encoding=utf-8
from functools import wraps
from sanic.response import json
# 登陆验证


def check_request_for_authorization_status(request):
    # cookie session，token校验，或 接口签名校验

    pass

# 装饰器
def authorized():
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            # run some method that checks the request
            # for the client's authorization status
            is_authorized = check_request_for_authorization_status(request)
            # 登陆验证
            if is_authorized:
                # the user is authorized.
                # run the handler method and return the response
                response = await f(request, *args, **kwargs)
                return response
            else:
                # the user is not authorized.
                return json({'status': 'not_authorized'}, 403)
        return decorated_function
    return decorator
