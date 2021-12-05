import base64
import requests
import os
import simple_aes


DIRECTORY = os.getcwd()


target_url = "https://driveimg1.intermarche.com/fr/Content/images/boitmal/produit/zoom/02DD0C00D2FB81CBA9735BD2FC6170B8.jpg"
number_node = 5
my_url = "http://localhost:8080/"

keys = ["key1", "key2", "key3", "key4", "key5"]


send_addresses = [
    "http://localhost:8082",
    "http://localhost:8083",
    "http://localhost:8084",
    "http://localhost:8085",
]

next_addr = "http://localhost:8081"
send_addresses.append("end_url+" + target_url)

return_addresses = [
    "http://localhost:8084",
    "http://localhost:8083",
    "http://localhost:8082",
    "http://localhost:8081",
    "http://localhost:8080",
]

addresses = send_addresses + return_addresses


def encrypt_address(send_addresses, return_addresses):
    encrypt_addr = ""
    for i in range(len(return_addresses) - 1, -1, -1):
        encrypt_addr = encrypt_message(
            (encrypt_addr + "$" + return_addresses[i] + "$"), keys[len(keys) - 1 - i]
        )
    for i in range(len(send_addresses) - 1, -1, -1):
        encrypt_addr = encrypt_message(
            (encrypt_addr + "$" + send_addresses[i] + "$"), keys[i]
        )
    return encrypt_addr


def send_packet(url, data):
    print("Sending !")
    print(len(data['addr']), len(data["content"]))
    requests.post(url, json=data)


def encrypt_message(message, key):
    # messageb64 = base64.b64encode(message.encode()).decode()
    ciphertext = simple_aes.encrypt(message, key)
    return ciphertext


def main():
    data = {"addr": encrypt_address(send_addresses, return_addresses), "content": ""}
    send_packet(next_addr, data)


if __name__ == "__main__":
    main()
