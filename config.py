# coding=UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# config.py创建基类Config来保存通用配置,其他的各环境使用不同的配置,再用一个字典提供选择

class Config(object):
    '''
    Common configurations
    '''

    #Put any configurations here that are common across all environments
    DEBUG=True

class DevelopmentConfig(Config):
    '''
    Development configurations
    '''

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    '''
    Production configurations
    '''

    DEBUG = False
    #确保生产环境下已经设置了 DEBUG = False。如果忘记关掉，用户会对服务器执行任意的Python代码

class TestingConfig(Config):
    # Testing configurations

    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}


