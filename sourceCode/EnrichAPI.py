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
            ip = ""
        try:
            hash = request.args["hash"]
        except:
            hash = ""
        try:
            mail = request.args["mail"]
        except:
            mail = ""
        try:
            domain = request.args["domain"]
        except:
            domain = ""
    data = app.run({"ip" : ip, "hash" : hash, "mail" : mail, "domain" : domain})
    return {"data" : data}




if __name__ == "__main__":
    api.run()