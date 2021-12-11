from flask import Flask, request
from flask.helpers import send_from_directory
import os


server = Flask(__name__)
DIRECTORY = os.getcwd()

@server.route("/tata", methods=["POST"])
def tata_sollicitation():
    data = request.get_data()
    r = data
    with open(DIRECTORY + "/tata.txt", "wb") as f:
        f.write(r)
    return "", 201

@server.route("/toto", methods=["POST"])
def toto_sollicitation():
    data = request.get_data()
    r = data
    with open(DIRECTORY + "/toto.txt", "wb") as f:
        f.write(r)
    return "", 201


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=8086, threaded=True)


