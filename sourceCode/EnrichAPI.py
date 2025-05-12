from lib.EnrichApp import EnrichApp

from flask import Flask, request

import time

api = Flask(__name__)
app = EnrichApp()

@api.route("/enrique", methods=['GET'])
def enrique():
    start = time.time()
    if request.method == 'GET':
        try:
            ip = request.args["ip"]
        except:
            ip = None
        try:
            hash = request.args["hash"]
        except:
            hash = None
        try:
            mail = request.args["mail"]
        except:
            mail = None
        try:
            url = request.args["url"]
        except:
            url = None
    data = app.run({"ip" : ip, "hash" : hash, "mail" : mail, "url" : url})
    return {"data" : data}




if __name__ == "__main__":
    api.run()