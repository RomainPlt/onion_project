# onion_project
recreate onion routing and try to hack it

## Setup python
- Install required python packages
```bash
pip install -r requirements.txt
```

## Get data out of wireshark

- Save your wireshark session as **.pcap** inside your project directory
- Install **tshark** 
```bash
sudo apt install tshark
```
- Extract data as json with tshark
```bash
tshark -T json -r my_data.pcap > my_data.json
```

