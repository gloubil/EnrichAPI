from waitress import serve
from EnrichAPI import api

if __name__ == '__main__':
    print("Serving...")
    serve(api, host='127.0.0.1', port=5002)


# http://localhost:5002/enrique?ip=95.111.239.171&hash=ba8cf312fcad02396f23c3f29ad2b5e4faf58bd0&mail=romain@debruille.fr&url=localhost