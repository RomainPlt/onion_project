import requests
import os
import simple_aes


DIRECTORY = os.getcwd()

file_to_send = input('Enter the name (or the whole path idk) of the file you want to send : \n')
end_point = input("Which end point do you want to reach ? \n")
target_url = "http://localhost:8086/" + end_point
number_node = 3
my_url = "http://localhost:8080"

with open(file_to_send) as f:
    data_to_send = f.read()

keys = ["key1", "key2", "key3"]


send_addresses = [
    "http://localhost:8082",
    "http://localhost:8083"
]

next_addr = "http://localhost:8081"
send_addresses.append("end_url+" + target_url)

def encrypt_address(send_addresses):
    encrypt_addr = ""
    for i in range(len(send_addresses) - 1, -1, -1):
        encrypt_addr = encrypt_message(
            (encrypt_addr + "$" + send_addresses[i] + "$"), keys[i]
        )
        print(len(encrypt_addr))
    return encrypt_addr


def send_packet(url, data):
    print("Sending !")
    print(len(data["addr"]), len(data["content"]))
    requests.post(url, json=data)


def encrypt_message(message, key):
    ciphertext = simple_aes.encrypt(message, key)
    return ciphertext


def main():
    data = {
        "addr": encrypt_address(send_addresses),
        "content": data_to_send,
    }
    send_packet(next_addr, data)


if __name__ == "__main__":
    main()
