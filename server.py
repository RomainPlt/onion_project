from flask import Flask, request
from flask.helpers import send_from_directory
import os
import requests
import json 
import aesgcm
import base64

server = Flask(__name__)
DIRECTORY= os.getcwd()

my_server_key = "romainpialatmaisimaginecest256bitslol"


@server.route("/files/<path:path>")
def get_file(path):
    return send_from_directory(DIRECTORY, path, as_attachment=True)


@server.route("/", methods=["POST"])
def server_sollicitation():  
    data = request.get_json()
    data = decrypt_data(data)
    print(data)
    to_server = data["to_server"]
    if to_server:
        addresses = data["send_addr"]
        next_address, method, addr_list = get_next_address(addresses)
        data["send_addr"] = addr_list
        forward(next_address, method, data)
        return "", 201
    else :
        addresses = data["return_addr"]
        next_address, method, addr_list = get_next_address(addresses)
        data["return_addr"] = addr_list
        forward(next_address, method, data)
        return "", 201

def decrypt_data(data):
    decrypted_data = {}
    for i in data:
        decrypted_tuple = {}
        if i != 'to_server':
            for j in data[i]:
                dec_key = decrypt_message(j)
                dec_value = decrypt_message(data[i][j])
                decrypted_tuple[dec_key] = dec_value
        elif i == 'to_server':
            decrypted_tuple[i] = data[i]
        decrypted_data[i] = decrypted_tuple
    return decrypted_data

def decrypt_message(ciphertext):
    key = my_server_key
    ciphertext = eval(ciphertext)
    res = aesgcm.main(ciphertext, key, False)
    return res.decode()

def get_next_address(addr_list):
    next_addr = list(addr_list.keys())[0]
    method = addr_list.pop(next_addr)
    return next_addr, method, addr_list

def forward(next_addr, method, data):
    if method == "post":
        r = requests.post(next_addr, json=data)
        return r.content.decode()
    elif method == "get":
        print("Last node")
        r = requests.get(next_addr, stream=True)
        data["to_server"] = False
        data["response"] = base64.b64encode(r.content)
        return send_back_response(data)

def send_back_response(data):
    addr_list = data["return_addr"]
    next_addr = list(addr_list.keys())[0]
    method = addr_list.pop(next_addr)
    if method == "post":
        r = requests.post(next_addr, json=data)
        return r.content.decode()
    else:
        return "wallah c cho tu fais nimp frerrrr"

if __name__ == "__main__":
    port = input("input port number : \n")
    my_address = "http://localhost:" + port
    server.run(
            host="0.0.0.0",
            port=port,
            threaded=True
      )