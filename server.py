# Should receive a message
# Decrypt it
# Get if it is the last hop or not
# If not last hop
    # Send to the next server
# Else
    # HTTP request to resolve


from flask import Flask, request
from flask.helpers import send_from_directory
import os

server = Flask(__name__)
UPLOAD_DIRECTORY= os.getcwd()


@server.route("/files/<path:path>")
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

@server.route("/", methods=["POST"])
def keep_going_or_not():  
    data = request.get_data().decode()
    if data == "":
        print("No more addresses : I AM THE ONLY ONE")
    else :
        next_address = get_next_address(data)
        forward(next_address)
    return "", 201

def forward(address):
    return 0

def get_next_address(addresses_list):
    return 0

if __name__ == "__main__":
    server.run(
            host="0.0.0.0",
            port=8081,
            threaded=True
        )