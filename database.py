from redis_om import get_redis_connection

redis = get_redis_connection(
    host="localhost",
    port=6379,
    password="redis",
    db=0,
    decode_responses=True,
)
