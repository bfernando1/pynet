#!/usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Parse the 'show version' output and look for the model and serial
         numbers of a device. 

Usage: 
    python exercise4.py

Output:
    Cisco in CISCO881-SEC-K9: True
    881 in CISCO881-SEC-K9: True
    
    Make: CISCO881-SEC-K9
    Serial: FTX0000038X
"""

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
fields = show_version.strip().split()

model = fields[1]
serial = fields[2]

make_in_model = 'cisco' in model.lower()
number_in_model = '881' in model

print(f"Cisco in {model}: {make_in_model}")
print(f"881 in {model}: {number_in_model}\n")

print(f"Make: {model}")
print(f"Serial: {serial}") 
