import json
from bottle import request
from bottle import get
from simple_eratosfen import is_simple


@get('/isprime')
def creation_handler():
    num = request.query.num
    result = is_simple(int(num))
    return json.dumps({'number': '{}'.format(num),
                       'is_prime': result})
