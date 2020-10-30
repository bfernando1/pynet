#! /usr/bin/env python3
"""Reads in a list in yaml and prints to standard output

Usage: 
    python3 ex-3a.yml

Output:
    ['Ethernet1', 'Ethernet2', 'Ethernet3', 'Ethernet4', 'Ethernet5', 'Ethernet6', 'Ethernet7', 'Management1', 'Vlan1']

Author: Bradley Fernando
"""
import yaml

with open("intf.yml") as f:
    output = yaml.load(f, Loader=yaml.Loader)
        
print(output)
