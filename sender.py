# Should encrypt n times a message
# Exchange keys with the n different servers
# Send message

import requests
from flask import Flask, request

my_url = "http://localhost:8080/"

url1 = "http://localhost:8081/"
url2 = "http://localhost:8082/"
url3 = "http://localhost:8083/"
url4 = "http://localhost:8084/"
final_url = "http://localhost:8085/files/toto.txt"

list_of_urls = [url2,url3,url4]

data = {"nodes_urls": list_of_urls, 
        "final_url": final_url,
        "sending_address": my_url}

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



def get_stuff(url):
    print(list_of_urls)
    r = requests.post(url, json=data, )
    print(r.content.decode())


client = Flask(__name__)

@client.route("/", methods=["POST"])
def get_response():
    data = request.get_json()
    print(data["response"])

if __name__ == "__main__":
    get_stuff(url1)
    client.run(
            host="0.0.0.0",
            port=8080,
            threaded=True
        )
