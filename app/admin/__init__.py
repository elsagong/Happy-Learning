# app/admin/__init__.py
# coding:UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import Blueprint

admin = Blueprint('admin', __name__)#文件夹or模块会从 Blueprint 的第二个参数中推断出来，通常是 __name__
#这个参数决定对应蓝图的是哪个逻辑的 Python 模块或包
from . import views# period. means current package
