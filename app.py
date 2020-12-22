import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count(key: str = 'hits'):
    retries = 5
    while True:
        try:
            return cache.incr(key)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello from Docker! I have been seen {count} times.\n'

@app.route('/cnt/<key>')
def inc_count(key: str):
    count = get_hit_count(key=key)
    return {
        'key': key,
        'count': count
    }
