from lib.EnrichApp import EnrichApp

from flask import Flask, request

api = Flask(__name__)
app = EnrichApp()

api.secret_key = "bijzbvhzribvjzrbvjoezbovzebnhieohvzreo"

@api.route("/enrique", methods=['GET'])
def enrique():
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
    return {"data" : app.run({"ip" : ip, "hash" : hash, "mail" : mail, "url" : url})}




if __name__ == "__main__":
    api.run()