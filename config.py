import os
import configparser
from dotenv import load_dotenv

load_dotenv()

config = configparser.ConfigParser()
config.read("settings.cfg")

DATABASE_BACKEND = config.get("database", "backend").lower()

print(DATABASE_BACKEND)

POSTGRES_URL = f"postgresql://{os.getenv("POSTGRES_USER")}:{os.getenv("POSTGRES_PASSWORD")}@{os.getenv("POSTGRES_HOST")}:{os.getenv("POSTGRES_PORT")}/{os.getenv("POSTGRES_DB")}"

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT"))
