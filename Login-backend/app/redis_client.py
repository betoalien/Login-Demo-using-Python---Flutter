# app/redis_client.py

import os
import redis
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read Redis configuration
REDIS_SERVER = os.getenv("REDIS_SERVER")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_USER = os.getenv("REDIS_USER", None)
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD", None)
REDIS_DECODE_RESPONSES = os.getenv("REDIS_DECODE_RESPONSES", "False").lower() == "true"

# Create a global Redis client instance (connection pool under the hood)
redis_client = redis.Redis(
    host=REDIS_SERVER,
    port=REDIS_PORT,
    username=REDIS_USER,
    password=REDIS_PASSWORD,
    decode_responses=REDIS_DECODE_RESPONSES,
)

def get_redis_client() -> redis.Redis:
    """
    Returns the global Redis client.
    This can be imported and used across the app.
    """
    return redis_client

# Optional: simple startup test (can be commented out in production)
if __name__ == "__main__":
    try:
        pong = redis_client.ping()
        print(f"✅ Redis connected: {pong}")
    except Exception as e:
        print(f"❌ Redis connection failed: {e}")
