class BaseConfig:
    SECRET_KEY = "dev-secret-key"
    DATABASE_URL = "mysql+pymysql://app_user:app_pass@localhost:3306/app_db"


class DevelopmentConfig(BaseConfig):
    TESTING = True
    DATABASE_URL = "mysql+pymysql://app_user:app_pass@localhost:3306/app_db"


class ProductionConfig(BaseConfig):
    DEBUG = False
    DATABASE_URL = "mysql+pymysql://app_user:app_pass@localhost:3306/app_db"
