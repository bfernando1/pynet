#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Reads in a file from a `show arp` output. Uses a loop to find the ip/
         mac addresses and prints them to standard output if it meets a
         condition. Once conditons are met, the loop terminates. 
         
Usage: 
    python exercise2.py

Output: 
    --------------------------------------------------------------------------------
    Default Gateway IP: 10.220.88.1
    MAC Address: 0062.ec29.70fe
    --------------------------------------------------------------------------------
    Arista3 IP/Mac: 10.220.88.30
    MAC Address: 5254.ab71.e119
    --------------------------------------------------------------------------------
"""

# Read in the file 'show arp' 
with open('show_arp.txt') as f:
    arp_lines = f.readlines()

arista3_ip, default_gw = '', ''
line_break = '-' * 80

# Parse through the 'show arp' output and store the ip/mac address 
for line in arp_lines:
    if line.startswith('Protocol'):
        continue
    ip_addr = line.split()[1]
    mac_addr = line.split()[3]
    
    # Look for the Default Gateway and Arista3 IP/MAC
    if ip_addr == '10.220.88.1':
        print(line_break)
        print(f"Default Gateway IP: {ip_addr}")
        print(f"MAC Address: {mac_addr}")
        print(line_break)
        default_gw = ip_addr
    elif ip_addr == '10.220.88.30':
        print(f"Arista3 IP/Mac: {ip_addr}")
        print(f"MAC Address: {mac_addr}")
        print(line_break)
        arista3_ip = ip_addr
    
    # Break out of loop once both IPs are found 
    if arista3_ip and default_gw:
        print("Found both IPs, exiting...")
        break
