#!/usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Prints 3 IP addresses to standard output

Usage: 
    python exercise1.py

Output:
    IP:      10.10.10.1
    IP:      10.10.10.2
    IP:      10.10.10.3
"""

ip_addr1 = "10.10.10.1"
ip_addr2 = "10.10.10.2"
ip_addr3 = "10.10.10.3"

ip_list = (
        f"IP: {ip_addr1:^20} \n"
        f"IP: {ip_addr2:^20} \n"
        f"IP: {ip_addr3:^20} ") 

print(ip_list) 
