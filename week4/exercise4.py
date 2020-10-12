#! /usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Takes the string output of 'show_version' and performs a regex serach
         to find the model and memory size. 
         
Usage: 
    python exercise4.py

Output:
    ----------------------------------------
              Model: 881
             Memory: 236544K/25600K
    ----------------------------------------
"""

line_div = '-' * 40

show_version = '''
Cisco 881 (MPC8300) processor (revision 1.0) with 236544K/25600K bytes of memory.
Processor board ID FTX0000038X

5 FastEthernet interfaces
1 Virtual Private Network (VPN) Module
256K bytes of non-volatile configuration memory.
126000K bytes of ATA CompactFlash (Read/Write)
'''

model = re.search(r"(Cisco) (?P<model_num>\w+)", 
                  show_version, flags=re.M).groupdict()

memory = re.search(r"(?P<memory_size>\w+K\/\w+K)",
                  show_version, flags=re.M).groupdict()

print(line_div)
print("{:>15}: {:20}".format('Model', model['model_num']))
print("{:>15}: {:20}".format('Memory', memory['memory_size']))
print(line_div)
