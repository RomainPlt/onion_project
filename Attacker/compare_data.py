import pandas as pd


def retrieve_data_from_wireshark(file):
    wjon = pd.read_json(file)
    shark = pd.DataFrame(wjon["_source"])
    data = dict(shark["_source"])
    return data


def check_http(frame):
    protocols = frame["layers"]["frame"]["frame.protocols"]
    if "http" in protocols:
        return True
    else:
        return False


def keep_http(data):
    http_data = {}
    for i in data:
        if check_http(data[i]):
            http_data[i] = data[i]
    return http_data


def clean_http(http):
    http_uselfull_data = {}
    for i in http:
        if list(http[i]["layers"]["http"].keys())[0] == "HTTP/1.0 201 CREATED\\r\\n":
            pass
        else:
            http_uselfull_data[i] = http[i]
    return http_uselfull_data


def drop_keys(http):
    key_to_remove = ["tcp.segments", "tcp", "json", "eth"]
    for i in http:
        for j in key_to_remove:
            try:
                http[i]["layers"].pop(j)
                pass
            except KeyError:
                print("There are no '", j, "' keys in here sorry")
    return http


def print_http_keys(http):
    for i in http:
        print(http[i]["layers"].keys())


def get_frame_len(http):
    length = http["layers"]["http"]["http.content_length_header"]
    return int(length)


def main():
    data = retrieve_data_from_wireshark("wireshark.json")
    http = keep_http(data)
    http = clean_http(http)
    http = drop_keys(http)
    lengths = []
    for i in http:
        lengths.append(get_frame_len(http[i]))
    return lengths


if __name__ == "__main__":
    main()
