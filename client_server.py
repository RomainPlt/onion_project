# sender server
import base64
from flask import Flask, request
import os

DOWNLOAD_DIRECTORY = os.getcwd() + "/image/"

client = Flask(__name__)

@client.route("/", methods=["POST"])
def get_response():
    data = request.get_json()
    r = data["response"]
    r = base64.b64decode(r)
    with open(DOWNLOAD_DIRECTORY + "oignon.png", 'wb') as f:
        f.write(r)
    return "", 201

if __name__ == "__main__":
    client.run(
            host="0.0.0.0",
            port=8080,
            threaded=True
        )
