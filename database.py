from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from redis import Redis
from config import POSTGRES_URL, REDIS_HOST, REDIS_PORT

engine = create_engine(POSTGRES_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
