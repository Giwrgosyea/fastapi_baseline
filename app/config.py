import os
import logging
from pydantic import BaseSettings
from constants import PROJECT_NAME, MONGO_HOST
from functools import lru_cache

basedir = os.path.abspath(os.path.dirname(__file__))


class Settings(BaseSettings):
    secret_key = os.getenv("SECRET_KEY", PROJECT_NAME + "_secret_key")
    debug = True
    mongo_database = PROJECT_NAME
    mongo_uri = "mongodb://" + MONGO_HOST + ":27017/" + mongo_database
    logging_level = logging.DEBUG
    enviroment = "development"
    max_connections_count = 10
    min_connections_count = 10


# class DevelopmentConfig(Config):
#     ENVIRONMENT = 'development'
#     USE_RELOADER = False
#     DEBUG = True
#     MONGO_URI = Config.MONGO_SERVER + ENVIRONMENT
#     LOGGING_LEVEL = logging.DEBUG
#
#
# class TestingConfig(Config):
#     ENVIRONMENT = 'testing'
#     DEBUG = True
#     TESTING = True
#     MONGO_URI = Config.MONGO_SERVER + ENVIRONMENT
#     LOGGING_LEVEL = logging.INFO
#
#
# class ProductionConfig(Config):
#     DEBUG = False
#     MONGO_URI = Config.MONGO_SERVER
#     LOGGING_LEVEL = logging.WARNING
#
#
# config_by_name = dict(
#     dev=DevelopmentConfig,
#     test=TestingConfig,
#     prod=ProductionConfig
# )


@lru_cache()
def get_settings() -> Settings:
    return Settings()
