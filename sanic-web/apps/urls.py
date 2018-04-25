#encoding=utf-8
import os

from . import app
# 静态配置


# 静态文件路径映射 配置（映射路径，实际路径，别名(使用home.别名 引用)）
# 例如要拿到 static目录下的file.txt  映射目录是 /home/static/file.txt

# 使用 app.url_for('static', name='home.static', filename='file.txt')的方式拿取
# 资源绑定url

# 这里注册了static url为/static,实际物理路径为../statics
# home.static('/static','../statics')

# 使用nginx 静态服务器，此处配置需改动
current_directory = app.config.BASE_DIR

static_directory = os.path.join(current_directory, 'statics')

# static 必须使用这种方式 使用相对路径不成功
# 使用nginx static 直接使用nginx配置路径需要重新配置
# app.static('/static',static_directory)

