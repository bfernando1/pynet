#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Reads in a file from `show ip bgp summary` output. It uses the .split()
         function to extract the AS number and BGP peer. 
         
Usage: 
    python exercise5.py

Output: 
    AS number: 42, BGP peer: 10.220.88.38
"""

from pprint import pprint

# Reads in a file and turns it into a list
with open('show_ip_bgp_summ.txt') as f:
    output = f.read()
output = output.splitlines()

# Parses the output for the AS number and the BGP Peer
as_num = output[0].split()[-1]
bgp_peer = output[-1].split()[0]

# Displays the results to standard output
print(f"AS number: {as_num}, BGP peer: {bgp_peer}")
