from ...log.logger import Logger

# from motor.motor_asyncio import AsyncIOMotorClient
from ...config import get_settings
from motor import connect, disconnect

# Function to connect in db

my_logger = Logger(__name__)
logger = my_logger.get_logger()
settings = get_settings()


async def connect_to_mongo():
    logger.info("Database Connection Initialization...")
    connect(db=settings.mongo_database, host=settings.mongo_uri)

    logger.info("Database Connection Initialization Sucess")


async def close_mongo_connection():
    logger.info("Database Connection Close...")
    disconnect()
    logger.info("Database Connection Close Sucess")
