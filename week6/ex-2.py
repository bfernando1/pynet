#! /usr/bin/env python3
"""Connects to a device using Netmiko and executes a show command

Usage:
    python ex-2.py

Output:
    --------------------------------------------------
    Running command: show ip route
    --------------------------------------------------
    Codes: L - local, C - connected, S - static, R - RIP, M - mobile, B - BGP
           D - EIGRP, EX - EIGRP external, O - OSPF, IA - OSPF inter area
           N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
           E1 - OSPF external type 1, E2 - OSPF external type 2
           i - IS-IS, su - IS-IS summary, L1 - IS-IS level-1, L2 - IS-IS level-2
           ia - IS-IS inter area, * - candidate default, U - per-user static route
           o - ODR, P - periodic downloaded static route, H - NHRP, l - LISP
           a - application route
           + - replicated route, % - next hop override, p - overrides from PfR

    Gateway of last resort is 10.220.88.1 to network 0.0.0.0

    S*    0.0.0.0/0 [1/0] via 10.220.88.1
          10.0.0.0/8 is variably subnetted, 2 subnets, 2 masks
    C        10.220.88.0/24 is directly connected, FastEthernet4
    L        10.220.88.20/32 is directly connected, FastEthernet4

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

# Command that Netmiko will run
command = 'show ip route'

with Netmiko(**cisco1) as net_connect:
    output = net_connect.send_command(command)

line_div = '-' * 50

print(line_div)
print(f"Running command: {command}")
print(line_div)
print(output)
