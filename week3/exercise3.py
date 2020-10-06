#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Reads in a file from a `show lldp neighbors` output. Uses a loop 
         to look for the System Name and Port ID/  
         
Usage: 
    python exercise3.py

Output: 
    System name: twb-sf-hpsw1
    Port: 15
"""

with open('show_lldp_neighbors_detail.txt') as f:
    output = f.read()

sys_name, port_id = None, None

for line in output.splitlines():
    if "System Name: " in line:
        # Take the last index of the 2 element list 
        _, sys_name = line.split("System Name: ")
    elif "Port id: " in line:
        _, port_id = line.split("Port id: ")
    if sys_name and port_id:
        break

print(f"System name: {sys_name}")
print(f"Port: {port_id}")
