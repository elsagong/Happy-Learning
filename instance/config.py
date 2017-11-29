# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#instance/config.py
#Flask提供了一个叫instance文件夹的特性,包括一个特定于当前应用实例的配置文件。不要把它提交到版本控制中。
#有时你需要定义一些不能为人所知的配置变量。为此，你会想要把它们从config.py中的其他变量分离出来，
#并保持在版本控制之外。 你可能要隐藏类似数据库密码和API密钥的秘密，或定义特定于当前机器的参数。
#instance文件夹的隐秘属性使得它成为藏匿密钥的好地方

SECRET_KEY = 'e-l-s-a'
SQLALCHEMY_DATABASE_URI = 'mysql://root:123321@localhost/dreamteam_db'

