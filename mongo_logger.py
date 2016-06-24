import datetime
import json
import os
from time import time
from pymongo import MongoClient


MONGO_HOSTS = os.getenv('MONGO_HOSTS', '127.0.0.1:27017')

def get_mongo_settings():
    return MONGO_HOSTS.split(',')

def log(f):
    def wrap(*args, **kwargs):
        start = time()
        result = f(*args, **kwargs)
        end = time()
        try:
            hosts = get_mongo_settings()
            client = MongoClient(hosts)
            db = client.test_database
            logs = db.logs
            data = json.loads(result)
            entry = {
                'number': data['number'],
                'date': datetime.datetime.utcnow(),
                'process_time': end - start
            }
            logs.insert_one(entry)
        except Exception, e:
            print('exception: {0}', e)
        finally:
            return result
    return wrap
