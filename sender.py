import requests
import os
import aesgcm

target_url = "https://assets.afcdn.com/story/20190220/1334066_w4912h2763c1cx2464cy1632cxt1084cyt0cxb4287cyb2983.jpg"
number_node = 5
my_url = "http://localhost:8080/"
my_key = "romainpialatmaisimaginecest256bitslol"

DIRECTORY= os.getcwd() 

def create_address_list(number_nodes):
    address_list = []
    return_addresses = [""]*number_nodes
    for i in range(number_nodes):
        address_list.append(encrypt_message("http://localhost:808"+str(i+1)))
        return_addresses[i] = encrypt_message("http://localhost:808"+str(number_nodes-i-1))
    return address_list, return_addresses

def create_dic_with_protocol(address_list):
    protocols = {}
    for i in address_list:
        protocols[i] = encrypt_message("post")
    return protocols 

def send_packet(url, data):
    requests.post(url, json=data)

def encrypt_message(message):
    key = my_key
    ciphertext = aesgcm.main(message, key, True)
    return str(ciphertext)

def decrypt_message(ciphertext):
    key = my_key
    ciphertext = eval(ciphertext)
    res = aesgcm.main(ciphertext, key, False)
    return res.decode()

def main():
    send_address, return_addr = create_address_list(number_node)
    send_addr_dic = create_dic_with_protocol(send_address)
    return_addr_dic = create_dic_with_protocol(return_addr)
    send_addr_dic[encrypt_message(target_url)] = encrypt_message("get")
    return_addr_dic[encrypt_message(my_url)] = encrypt_message("post")
    next_addr = list(send_addr_dic.keys())[0]
    send_addr_dic.pop(next_addr)
    data = {"send_addr" : send_addr_dic,
            "return_addr" : return_addr_dic,
            "to_server": True}
    next_addr = decrypt_message(next_addr)
    print(next_addr)
    send_packet(next_addr, data)

if __name__ == "__main__":
    main()
