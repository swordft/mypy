class DevelopmentConfig():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://ucloudlink:123456@192.168.50.66/test'

class ProductionConfig():
    SQLALCHEMY_DATABASE_URI = 'mysql://ucloudlink:123456@192.168.50.66/product'

config = {
    'dev': DevelopmentConfig,
    'pro': ProductionConfig,
    'default': DevelopmentConfig
}
