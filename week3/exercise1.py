#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Reads in a file from a `show vlan` output. Uses a loop to extract all 
         of the VLAN IDs and numbers into a separate tuple. 
         
Usage: 
    python exercise1.py

Output: 
    [('1', 'default'), ('400', 'blue400'), ('401', 'blue401'), ('402', 'blue402'), ('403', 'blue403')]    
"""

with open('show_vlan.txt') as f:
    output = f.readlines()

vlan_list = []

for line in output:
    if 'VLAN' in line or '-----' in line or line.startswith('   '):
        continue
    vlan_num = line.split()[0]
    vlan_id = line.split()[1]
    vlan_list.append((vlan_num, vlan_id))

print(vlan_list)
