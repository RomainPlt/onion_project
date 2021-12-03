import base64
import requests
import os

import simple_aes_cipher
import simple_aes
import aesgcm

DIRECTORY= os.getcwd() 


target_url = "https://driveimg1.intermarche.com/fr/Content/images/boitmal/produit/zoom/02DD0C00D2FB81CBA9735BD2FC6170B8.jpg"
number_node = 5
my_url = "http://localhost:8080/"

keys = ["key1", "key2", "key3", "key4", "key5"]
send_addresses = ["http://localhost:8082","http://localhost:8083",
"http://localhost:8084","http://localhost:8085"]
next_addr = "http://localhost:8081"
send_addresses.append("end_url+"+target_url)

return_addresses = ["http://localhost:8084","http://localhost:8083",
"http://localhost:8082","http://localhost:8081","http://localhost:8080"]

addresses = send_addresses + return_addresses

def encrypt_address(send_addresses, return_addresses):
    encrypt_addr = ""
    for i in range(len(return_addresses)-1, -1, -1):
        encrypt_addr = encrypt_message(encrypt_addr + "$" + return_addresses[i] + "$")
    for i in range(len(send_addresses)-1, -1, -1):
        encrypt_addr = encrypt_message(encrypt_addr + "$"+send_addresses[i]+"$")
    return encrypt_addr

def create_address_list(number_nodes):
    address_list = []
    return_addresses = [""]*number_nodes
    for i in range(number_nodes):
        address_list.append(("http://localhost:808"+str(i+1)))
        return_addresses[i] = ("http://localhost:808"+str(number_nodes-i-1))
    return address_list, return_addresses



def send_packet(url, data):
    print(data)
    requests.post(url, json=data)

def encrypt_message(message):
    messageb64 = base64.b64encode(message.encode()).decode()
    # ciphertext = simple_aes.encrypt(messageb64, key)
    return messageb64

def decrypt_message(ciphertext, key):
    plaintext = simple_aes.decrypt(ciphertext, key)
    return plaintext

def encrypt_data(data):
    for i in data:
        if i == "to_server":
            break
        for j in range(len(data[i])):
            for k in range(j, len(data[i])):
                enc_addr = encrypt_message(data[i][k], key=keys[j])
                print(k, enc_addr)
                data[i][k] = enc_addr
    return data


def main():
    data = {"addr" : encrypt_address(send_addresses, return_addresses),
        "content" : ""}
    send_packet(next_addr, data)

if __name__ == "__main__":
    main()
