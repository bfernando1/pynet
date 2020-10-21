#! /usr/bin/env python3 
"""Connects to a device using Netmiko and prints the prompt
Usage:
    python ex-1.py
Output:
    Password:
    cisco1#
Author: Bradley Fernando
"""

from netmiko import Netmiko
from getpass import getpass

cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": getpass()
}

net_conn = Netmiko(**cisco1)
print(net_conn.find_prompt())
