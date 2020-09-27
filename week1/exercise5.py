#!/usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Takes the output from 'show arp' and displays the ip and mac address 
         in a table formatted with 20 spaces, right aligned. 
         

Usage: 
    python exercise5.py

Output:
                 IP ADDR         MAC ADDRESS
    -------------------- --------------------
            10.220.88.29      5254.abbe.5b7b
            10.220.88.30      5254.ab71.e119
            10.220.88.32      5254.abc7.26aa
"""



mac1 = "Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4"
mac2 = "Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4"
mac3 = "Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4"

mac_addr1, ip_addr1 = mac1.split()[1], mac1.split()[3]
mac_addr2, ip_addr2 = mac2.split()[1], mac2.split()[3]
mac_addr3, ip_addr3 = mac3.split()[1], mac3.split()[3]

print("{:>20}{:>20}".format("IP ADDR", "MAC ADDRESS"))
print('-' * 20 + ' ' + '-' * 20)
print("{:>20}{:>20}".format(mac_addr1, ip_addr1))
print("{:>20}{:>20}".format(mac_addr2, ip_addr2))
print("{:>20}{:>20}".format(mac_addr3, ip_addr3))
