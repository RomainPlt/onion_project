from flask import Flask, request
from flask.helpers import send_from_directory
import os
import requests
import json
import aesgcm
import base64
import simple_aes

server = Flask(__name__)
DIRECTORY = os.getcwd()


@server.route("/files/<path:path>")
def get_file(path):
    return send_from_directory(DIRECTORY, path, as_attachment=True)


@server.route("/", methods=["POST"])
def server_sollicitation():
    req = request.get_json()
    print(req)
    print("Received !")
    req, next_addr = get_address(req)
    print("\n", next_addr)
    return post_data(next_addr, req)


def get_address(req):
    data = req["addr"]
    data = simple_aes.decrypt(data, key)
    data = base64.b64decode(data.encode()).decode()
    print(data)
    for i in range(len(data)):
        addr = ""
        if data[i] == "$" and data[i + 1 : i + 5] == "http":
            print("\nGoing for the post\n")
            for j in range(i + 1, len(data)):
                if data[j] == "$":
                    break
                addr += data[j]
            data = data.replace(data[i : i + j], "")
            req["addr"] = data
            return req, addr

        elif data[i] == "$" and data[i + 1 : i + 9] == "end_url+":
            print("\nGoing for the get\n")
            for j in range(i + 9, len(data)):
                if data[j] == "$":
                    break
                addr += data[j]
            data = data.replace(data[i : i + j], "")
            req["addr"] = data
            req["content"] = get_content(addr)
            return get_address(req)


def get_content(addr):
    r = requests.get(addr, stream=True)
    return base64.b64encode(r.content).decode()


def post_data(addr, data):
    print("posting to :", addr)
    print(data)
    r = requests.post(addr, json=data)
    return "", 201


if __name__ == "__main__":
    port = input("input port number : \n")
    key = input("What's the key ? \n")
    my_address = "http://localhost:" + port
    server.run(host="0.0.0.0", port=port, threaded=True)
