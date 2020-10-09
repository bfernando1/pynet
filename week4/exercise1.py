#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Creates a network device and bgp dictionary and merges them. Prints the 
         keys and values to standard output.

Usage: 
    python exercise1.py

Output:
    ------------------------------
    10.150.0.20
    ------------------------------
    {'bgp_as': 100,
     'ip_addr': '10.150.0.20',
     'password': 'admin',
     'peer_as': 200,
     'peer_ip': '192.168.7.2',
     'platform': 'junos',
     'username': 'netadmin',
     'vendor': 'juniper'}
    ------------------------------
    juniper
    junos
    10.150.0.20
    netadmin
    admin
    100
    200
    192.168.7.2
    ------------------------------
    key: vendor
    value: juniper
    ------------------------------
    key: platform
    value: junos
    ------------------------------
    key: ip_addr
    value: 10.150.0.20
    ------------------------------
    key: username
    value: netadmin
    ------------------------------
    key: password
    value: admin
    ------------------------------
    key: bgp_as
    value: 100
    ------------------------------
    key: peer_as
    value: 200
    ------------------------------
    key: peer_ip
    value: 192.168.7.2
    ------------------------------
"""
from pprint import pprint
line_divider = '-' * 30


net_device = {'vendor': 'juniper', 
              'platform': 'junos',
              'ip_addr': '10.150.0.20',
              'username': 'netadmin',
              'password': 'admin'
}

bgp_fields = {'bgp_as': 100,
              'peer_as': 200,
              'peer_ip': '192.168.7.2'
}


print(line_divider)
print(net_device.get('ip_addr'))
print(line_divider)

# Merge bgp dictionary with devices 
net_device.update(bgp_fields)
pprint(net_device)


print(line_divider)
for values in net_device.values():
    print(values)

print(line_divider)
for key, value in net_device.items():
    print(f"key: {key}")
    print(f"value: {value}")
    print(line_divider)
