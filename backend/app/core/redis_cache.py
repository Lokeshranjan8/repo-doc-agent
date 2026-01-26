import os
import redis 
from dotenv import load_dotenv
import json
load_dotenv

redis_url = os.getenv("REDIS_URL","redis://localhost:6379")
redis_client = redis.from_url(redis_url)

def get_cache(key: str):
    cache_data = redis_client.get(key)
    if cache_data :
        return json.loads(cache_data)
    return None



def set_cache(key: str, value, expire: int=180):
    redis_client.set(key,json.dumps(value),ex=expire)
