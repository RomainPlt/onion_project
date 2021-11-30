# Should encrypt n times a message
# Exchange keys with the n different servers
# Send message

import requests
from flask import Flask, request

target_url = "https://assets.afcdn.com/story/20190220/1334066_w4912h2763c1cx2464cy1632cxt1084cyt0cxb4287cyb2983.jpg"
number_node = 5
my_url = "http://localhost:8080/"

def create_address_list(number_nodes):
    address_list = []
    for i in range(number_nodes):
        address_list.append("http://localhost:808"+str(i+1))
    return address_list

def create_dic_with_protocol(address_list):
    protocols = {}
    for i in address_list:
        protocols[i] = "post"
    return protocols 

def send_packet(url, data):
    r = requests.post(url, json=data )
    print(r.content.decode())

def main():
    address_dic = create_dic_with_protocol(create_address_list(number_node))
    address_dic[target_url] = "get"
    print(address_dic)
    next_addr = list(address_dic.keys())[0]
    address_dic.pop(next_addr)
    send_packet(next_addr, address_dic)


client = Flask(__name__)

@client.route("/", methods=["POST"])
def get_response():
    data = request.get_json()
    print(data["response"])

if __name__ == "__main__":
    main()
    client.run(
            host="0.0.0.0",
            port=8080,
            threaded=True
        )
