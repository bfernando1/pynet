#!/usr/bin/env python3 

"""
Author: Bradley Fernando
Purpose: Converts IPs to hexidecimal and binary format. Displays the output into
         a table. 

Usage: 
    python exercise2.py

Output:
    Please enter an IP address: 80.98.100.240
        Octet1         Octet2         Octet3         Octet4
    ------------------------------------------------------------
          80             98             100            240
       0b1010000      0b1100010      0b1100100     0b11110000
         0x50           0x62           0x64           0xf0
    ------------------------------------------------------------
"""


ipaddr = input("Please enter an IP address: ")
ip_list= ipaddr.split('.')

# Convert to list of integers for binary/hex conversion 
octets = [int(i) for i in ip_list]

# Format each column by 15 spaces and make it centered 
spacing = "{:^15}{:^15}{:^15}{:^15}"

# Print table header 
print(spacing.format('Octet1','Octet2','Octet3','Octet4'))
print("-" * 60)

# Print original/binary/hex converted IPs  
print(spacing.format(octets[0], octets[1], octets[2], octets[3]))
print(spacing.format(bin(octets[0]), bin(octets[1]), bin(octets[2]), bin(octets[3])))
print(spacing.format(hex(octets[0]), hex(octets[1]), hex(octets[2]), hex(octets[3])))

print("-" * 60)
