#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Take output from 'show ipv6 intf' and looks for ipv6 addresses using 
         the DOTALL regex flag. Displays the results to standard output. 

Usage: 
    python exercise5.py
Output:
    --------------------------------------------------
    IPv6 Addresses Found:
        1. 2001:11:2233::a1/24
        2. 2001:cc11:22bb:0:2ec2:60ff:fe4f:feb2/64
    --------------------------------------------------
"""
import re 

with open('show_ipv6_intf.txt') as f:
    output = f.read()

# Look for IPs up until the line containing 'IPv6 subnet' 
parse_ipv6 = re.search(r"(\d{4}.*)\s+IPv6 subnet:", 
                      output, flags=re.DOTALL).group(1)

# Turn the regex matches into a list
split_ipv6 = parse_ipv6.strip().split(' ')

ipv6_list = []

# Add strings with ':' to the IPv6 list 
for ipv6 in split_ipv6:
    if ':' in ipv6:
        ipv6_list.append(ipv6)

# Display the results
line_div = '-' * 50

print(line_div)

print('IPv6 Addresses Found:')
for num, found_ips in enumerate(ipv6_list):
    print("{:>5}. {:10}".format((num + 1), found_ips))

print(line_div)
