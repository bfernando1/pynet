#! /usr/bin/env python3
"""Deletes a file from flash on a cisco device

Usage:
    python ex-3.py

Output:
    del flash:/bf-test.txt
    Delete filename [bf-test.txt]?
    Delete flash:/bf-test.txt? [confirm]y
    cisco1#
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

command = "del flash:/bf-test.txt"
net_connect = Netmiko(**cisco1)

output = net_connect.send_command_timing(
    command_string=command, strip_prompt=False, strip_command=False
)

if "Delete filename" in output:
    output += net_connect.send_command_timing(
        command_string="\n", strip_prompt=False, strip_command=False
    )

if "confirm" in output:
    output += net_connect.send_command_timing(
        command_string="y", strip_prompt=False, strip_command=False
    )

net_connect.disconnect()

print(f"\n{output}\n")
