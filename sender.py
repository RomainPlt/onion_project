# Should encrypt n times a message
# Exchange keys with the n different servers
# Send message

import requests

url1 = "http://localhost:8081/"
url2 = "http://localhost:8082/"
url3 = "http://localhost:8083/"
url4 = "http://localhost:8084/toto.txt"


list_of_urls = url2+";"+url3+";"+url4+";"

def get_stuff(url):
    print(list_of_urls)
    r = requests.post(url= url, data=list_of_urls)
    print(r.content.decode())

if __name__ == "__main__":
    get_stuff(url1)