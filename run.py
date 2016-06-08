import bottle
import api


app = application = bottle.default_app()

def start_service(host,port):
    bottle.run(host=host, port=port)

#TODO
def stop_service():
    pass


if __name__ == '__main__':
    bottle.run(host='127.0.0.1', port=12000)
