# onion_project
Recreate onion routing and try to hack it.
All servers are *Flask* servers.

## Setup python
* Install required python packages
```bash
pip install -r requirements.txt
```

## Setup your local onion routing
* You can add as many onion routers as you want, just go to the **Tor_nodes** directory and run *python3 server.py* in different terminals.
* For each tor router you will be asked a port and a key, if you're running this on local host for every routers do not use the same port !

## Setup your end server
* Go to your **End_server** directory and run the *end_server.py* file.
* This server listens on *localhost:8086*

## Setup your client
* Go to the **Client** directory
* If your file *sender.py* is already on fleek you'll just have to run it
* Else edit it and change those options : 
`* target_url = 'the_address_of_your_end_server'`
`* number_node = the_number_of_onion_routers_you've_set_up`
`* keys list = ['1st_node_key', '2nd_node_key', 'etc']`
`* send_addresses = ['2nd_onion_router', '3rd_onion_router', 'etc']`
`* next_addr = '1st_onion_router_address'`
* You can also edit the file you send by placing one of yours instead of the "classic_french" stuff that we use here.

## Sniff on the network
* Here we're talking about local network so there are no such things as *entry router* or *exit router*, you can just run **wireshark** and listen to all the trafic going on your computer.
* You'll see that the payload is diminishing during the transfer, to find the length a payload had while entering the "tor" network you should go to the **Attacker** directory and run *correlation.py*.
* Using the "dataframe.csv" file in this directory, *correlation.py* will give you an approximation of the entry length of a payload, regarding its exit length.



