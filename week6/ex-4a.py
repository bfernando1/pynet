#! /usr/bin/env python3
"""Configures a network device using Netmiko send_config_set command 
Usage:
    pyton ex-4a.py
Output:
    configure terminal
    Enter configuration commands, one per line.  End with CNTL/Z.
    cisco1(config)#logging buffered 100000
    cisco1(config)#end
    cisco1#write mem
    Building configuration...
    [OK]
    cisco1#
Author: Bradley Fernando
"""
from netmiko import Netmiko
from getpass import getpass

password = getpass()

cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": password
}       

commands = ["logging buffered 100000"]
with Netmiko(**cisco1) as net_connect:
    output = net_connect.send_config_set(commands)
    output += net_connect.save_config()

print(f"\n{output}\n")
