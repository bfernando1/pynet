#! /usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Reads a file from `show ip int brief` and looks for a specific
         interface. Stores the results into a tuple and prints the output.
         
Usage: 
    python exercise4.py

Output: 
    ('FastEthernet4', '10.220.88.20')
"""
from pprint import pprint

with open("show_ip_int_brief.txt") as f:
    output = f.readlines()

# extract a specific interface from the file
interface, ip = output[5].split()[0], output[5].split()[1]

# place the results into a tuple
port_list = (interface, ip)

# print the results to standard output
print(port_list)
