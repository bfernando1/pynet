#! /usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Takes a file with ARP entries and does a series of list operations. The
         final result will create a new file. 

Usage: 
    python exercise3.py

Output: 
    ...
    <snipped for brevity>
    ...
    ('Internet  10.220.88.1           135   0062.ec29.70fe  ARPA   FastEthernet4\n'
     
     'Internet  10.220.88.20            -   c89c.1dea.0eb6  ARPA   FastEthernet4\n'
    
     'Internet  10.220.88.21          213   1c6a.7aaf.576c  ARPA   FastEthernet4\n')
"""
from pprint import pprint 

# import the file `show_arp.txt`, convert to a list, remove the header 
with open("show_arp.txt") as f:
   output = f.readlines()

arp_list = output[1:]
pprint(arp_list)

# sort based on IPs 
pprint(arp_list.sort())

# create a new list containing the first 3 ARP entries
arp_sliced = arp_list[:3]
pprint(arp_sliced)

# join the new list 
arp_sliced = '\n'.join(arp_sliced)
pprint(arp_sliced)

# write the list out to a file 
with open("arp_entries.txt", "w") as f:
    f.write(arp_sliced)
