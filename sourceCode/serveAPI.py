from waitress import serve
from EnrichAPI import api

if __name__ == '__main__':
    print("Serving...")
    serve(api, host='127.0.0.1', port=5002)


# ip : http://localhost:5002/enrique?ip=10.81.101.151
# hash : http://localhost:5002/enrique?hash=SHA1:ba8cf312fcad02396f23c3f29ad2b5e4faf58bd0
# domain : http://localhost:5002/enrique?domain=etu.univ-tours.fr
# mail : http://localhost:5002/enrique?mail=romain.debruille@etu.univ-tours.fr

# several : http://localhost:5002/enrique?ip=218.92.0.147&hash=SHA1:ba8cf312fcad02396f23c3f29ad2b5e4faf58bd0&domain=etu.univ-tours.fr&mail=romain.debruille@etu.univ-tours.fr

# N8N Basic Request : http://localhost:5002/enrique?ip=218.92.0.147&hash=&domain=&mail=

# 146.70.42.228

# TODO Données Fausses sur le InfoTool -> Fact checker les infos récupérées