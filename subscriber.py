import redis

with redis.Redis() as client:
    pubsub = client.pubsub()