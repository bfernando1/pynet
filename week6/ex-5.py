#! /usr/bin/env python3
"""Converts 'show ip route' into structered data using TextFSM
# git clone https://github.com/networktocode/ntc-templates.git
# into home directory

Usage:
    python ex-5.py

Output:
    --------------------------------------------------
    Running command: show ip route
    --------------------------------------------------
    [{'distance': '1',
      'mask': '0',
      'metric': '0',
      'network': '0.0.0.0',
      'nexthop_if': '',
      'nexthop_ip': '10.220.88.1',
      'protocol': 'S',
      'type': '',
      'uptime': ''},
     {'distance': '',
      'mask': '24',
      'metric': '',
      'network': '10.220.88.0',
      'nexthop_if': 'FastEthernet4',
      'nexthop_ip': '',
      'protocol': 'C',
      'type': '',
      'uptime': ''},
     {'distance': '',
      'mask': '32',
      'metric': '',
      'network': '10.220.88.20',
      'nexthop_if': 'FastEthernet4',
      'nexthop_ip': '',
      'protocol': 'L',
      'type': '',
      'uptime': ''}]
Author: Bradley Fernando
"""

from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

password = getpass()

cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": password
}

# Command that Netmiko will run
command = 'show ip route'

with Netmiko(**cisco1) as net_connect:
    output = net_connect.send_command(command, use_textfsm=True)

line_div = '-' * 50

print(line_div)
print(f"Running command: {command}")
print(line_div)
pprint(output)
