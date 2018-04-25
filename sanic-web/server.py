#encoding=utf-8
from apps.home import home as home_blue_print
from apps.login import login as login_blue_print
from apps import app


# 注册蓝本
app.blueprint(home_blue_print)
app.blueprint(login_blue_print)

# print(app.config.DEBUG)

if __name__ == "__main__": # 使用这种方式将其包装起来，以便它只在解释器直接运行时执行。

    # print(app.url_for('static', name='static', filename='file.txt'))
    # print(app.config.BASE_DIR)
    # /home/static/file.txt
    app.run(host='0.0.0.0', port=8000,workers=1, debug=app.config['DEBUG'],access_log=True)
    # access_log = True/False 可以使用自己的日志配置 logging ，自带三种日志，可以参考官网
    # works多进程，多核心，数量参考cpu的核心数


# 部署 有2种方式，2种我都试过，推荐第2种Gunicorn ，官方说，可以减少内存泄漏的影响
'''
第一种
python -m sanic server.app --host=0.0.0.0 --port=1337 --workers=1

(venv) Grabbys-MacBook-Pro:sanic-web grabbywu$ python -m sanic server.app --host=0.0.0.0 --port=1337 --workers=1
[2018-04-24 22:10:45 +0800] [1496] [INFO] Goin' Fast @ http://0.0.0.0:1337
[2018-04-24 22:10:45 +0800] [1496] [INFO] Starting worker [1496]
Server successfully started!
^C
[2018-04-24 22:11:42 +0800] [1496] [INFO] Stopping worker [1496]
[2018-04-24 22:11:42 +0800] [1496] [INFO] Server Stopped

'''
'''
第二种 http://docs.gunicorn.org/en/latest/install.html
gunicorn server:app --bind 0.0.0.0:1337 --worker-class sanic.worker.GunicornWorker


(venv) Grabbys-MacBook-Pro:sanic-web grabbywu$ gunicorn server:app --bind 0.0.0.0:1337 --worker-class sanic.worker.GunicornWorker
[2018-04-24 22:17:22 +0800] [1543] [INFO] Starting gunicorn 19.7.1
[2018-04-24 22:17:22 +0800] [1543] [INFO] Listening at: http://0.0.0.0:1337 (1543)
[2018-04-24 22:17:22 +0800] [1543] [INFO] Using worker: sanic.worker.GunicornWorker
[2018-04-24 22:17:22 +0800] [1546] [INFO] Booting worker with pid: 1546
Server successfully started!
[2018-04-24 22:17:52 +0800] - (sanic.access)[INFO][1:2]: GET http://0.0.0.0:1337/  200 51
[2018-04-24 22:17:53 +0800] - (sanic.access)[INFO][1:2]: GET http://0.0.0.0:1337/favicon.ico  200 62
[2018-04-24 22:17:58 +0800] [1546] [INFO] KeepAlive Timeout. Closing connection.
^C[2018-04-24 22:18:00 +0800] [1543] [INFO] Handling signal: int
[2018-04-24 22:18:01 +0800] [1546] [INFO] Stopping server: 1546, connections: 1
[2018-04-24 22:18:01 +0800] [1546] [INFO] Error while closing socket [Errno 9] Bad file descriptor
[2018-04-24 22:18:01 +0800] [1546] [INFO] Worker exiting (pid: 1546)
[2018-04-24 22:18:01 +0800] [1543] [INFO] Shutting down: Master

'''

