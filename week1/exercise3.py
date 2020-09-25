#!/usr/bin/env python3 

"""
Author: Bradley Fernando
Purpose: Compares the values of 3 variables that are name formatted in 
         different ways. 

Usage: 
    python exercise3.py

Output:
    ip_address equal to IP_ADDRESS: True
    ip_address equal to IP_ADDRESS_1: False
"""


ip_address = "::1"
IP_ADDRESS = "::1"
IP_ADDRESS_1 = "fe80::aede:48ff:fe00:1111"

compare1_2 = ip_address == IP_ADDRESS
compare1_3 = ip_address == IP_ADDRESS_1

print(f"ip_address equal to IP_ADDRESS: {compare1_2}")
print(f"ip_address equal to IP_ADDRESS_1: {compare1_3}")
