import aioredis

from config import config

redis = aioredis.from_url(url=f"redis://{config.REDIS_HOST}")
