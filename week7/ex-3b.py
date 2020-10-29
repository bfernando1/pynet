#! /usr/bin/env python3
"""Reads in a list of nested yaml dictionaries and displays them to stdout

Usage: 
    python3 ex-3b.yml

Output:
    {'interfaces': {'Ethernet1': {'mode': 'access', 'vlan': 10},
                    'Ethernet2': {'mode': 'access', 'vlan': 20},
                    'Ethernet3': {'mode': 'trunk',
                                  'native_vlan': 1,
                                  'trunk_vlan': 'all'}}}

Author: Bradley Fernando
"""
import yaml
from pprint import pprint

with open("intf-3b.yml") as f:
    output = yaml.load(f, Loader=yaml.Loader)
        
pprint(output)
