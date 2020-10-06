#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Takes a tuple containing the IP and MAC address and extracts the
         MAC addresses. It formats the MAC from '.' to ':' separated. 
         
Usage: 
    python exercise1.py

Output: 
    00:62:EC:29:70:FE
    C8:9C:1D:EA:0E:B6
    1C:6A:7A:AF:57:6C
    52:54:AB:A8:9A:EA
    52:54:AB:BE:5B:7B
    52:54:AB:71:E1:19
    52:54:AB:C7:26:AA
    52:54:AB:3A:8D:26
    52:54:AB:FB:AF:12
    00:01:00:FF:00:01
    00:02:00:FF:00:01
    64:64:9B:E8:08:C8
    00:1C:C4:BF:82:6A
    00:1B:78:73:56:34
"""

arp_table = \
[('10.220.88.1', '0062.ec29.70fe'),
 ('10.220.88.20', 'c89c.1dea.0eb6'),
 ('10.220.88.21', '1c6a.7aaf.576c'),
 ('10.220.88.28', '5254.aba8.9aea'),
 ('10.220.88.29', '5254.abbe.5b7b'),
 ('10.220.88.30', '5254.ab71.e119'),
 ('10.220.88.32', '5254.abc7.26aa'),
 ('10.220.88.33', '5254.ab3a.8d26'),
 ('10.220.88.35', '5254.abfb.af12'),
 ('10.220.88.37', '0001.00ff.0001'),
 ('10.220.88.38', '0002.00ff.0001'),
 ('10.220.88.39', '6464.9be8.08c8'),
 ('10.220.88.40', '001c.c4bf.826a'),
 ('10.220.88.41', '001b.7873.5634')]

# Convert to just HEX block, no dotted decimal
for ip_addr, mac_addr in arp_table:
    mac_addr = mac_addr.split('.')
    mac_addr = "".join(mac_addr)
    mac_addr = mac_addr.upper()
    
    # Separate the HEX block into 2 character pairs
    new_list = []
    while len(mac_addr) > 0:
        new_mac = mac_addr[:2]
        mac_addr = mac_addr[2:]
        new_list.append(new_mac)
    
    # Reattach the HEX block using a ':'
    new_mac = ":".join(new_list)
    print(new_mac)
