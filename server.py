from flask import Flask, request
from flask.helpers import send_from_directory
import os
import requests

server = Flask(__name__)
UPLOAD_DIRECTORY= os.getcwd()

class Server:
    def __init__(self, precendent_address, next_address, my_addr):
        self.prec_addr = precendent_address
        self.next_addr = next_address
        self.addr = my_addr

    def send_packet(self, next_address, other_nodes_address, my_addr, final_addr):
        data = {"nodes_urls": other_nodes_address,
                "final_url": final_addr,
                "sending_address": my_addr}
        print("Sending ", data, " to ", next_address)
        r = requests.post(next_address, json=data)
        return r.content.decode()


@server.route("/files/<path:path>") # send back toto.txt
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)


@server.route("/", methods=["POST"])
def server_sollicitation():  
    data = request.get_json()
    nodes = data["nodes_urls"]
    precedent = data["sending_address"]
    final = data["final_url"]    
    if nodes == []:
        print("Out of Tor network")
        r = requests.get(final)
        print(r.content.decode())
    else :
        print("Forwarding ...")
        next_address, address_list = get_next_address(nodes)
        my_server = Server(precedent, next_address, my_address)
        my_server.send_packet(next_address, address_list, my_address, final)
    return "", 201

def forward(next_adress, other_nodes_address, final_address):
    data = {"nodes_urls": other_nodes_address,
            "final_url": final_address}
    print("Sending ", data, " to ", next_adress)
    r = requests.post(next_adress, json=data)
    return r.content.decode()

def get_next_address(addresses_list):
    next_addr = addresses_list[0]
    other_nodes = addresses_list[1:]
    return next_addr, other_nodes

if __name__ == "__main__":
    port = input("input port number : \n")
    my_address = "http://localhost:" + port
    server.run(
            host="0.0.0.0",
            port=port,
            threaded=True
        )