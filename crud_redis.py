import json
from redis import Redis
from schemas import UserCreate

def _redis_key(user_id: int) -> str:
    return f"user:{user_id}"

def get_user(r: Redis, user_id: int):
    data = r.get(_redis_key(user_id))
    return json.loads(data) if data else None

def create_user(r: Redis, user: UserCreate):
    key = _redis_key(user.id)
    if r.exists(key):
        return None
    r.set(key, json.dumps(user.model_dump()))
    return user.model_dump()

def update_user(r: Redis, user_id: int, user: UserCreate):
    key = _redis_key(user_id)
    if not r.exists(key):
        return None
    r.set(key, json.dumps(user.model_dump()))
    return user.model_dump()

def delete(r: Redis, user_id: int):
    key = _redis_key(user_id)
    data = r.get(key)
    if not data:
        return None
    r.delete(key)
    return json.loads(data)
