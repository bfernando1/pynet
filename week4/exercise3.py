#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Reads in a file containing a 'show_version' output and uses regex
         to find and print the values for the following:
            - software version
            - serial number
            - config register 

Usage: 
    python exercise3.py

Output:
    ------------------------------------------------------------
              OS Version: 15.4(2)T1
           Serial Number: FTX0000038X
         Config Register: 0x2102
    ------------------------------------------------------------
"""
import re 

with open('show_version.txt') as f:
    output = f.read()

version = re.search(r"(Version (?P<sw_version>.*),)", 
                    output, flags=re.M).groupdict()

serial = re.search(r"(Processor board ID) (?P<serial_num>\w+)", 
                    output, flags=re.M).groupdict()

confreg = re.search(r"(Configuration register is) (?P<confreg_num>\w+)$", 
                    output, flags=re.M).groupdict()

line_div = '-' * 60

print(line_div)
print("{:>20}: {:15}".format('OS Version', version['sw_version']))
print("{:>20}: {:15}".format('Serial Number', serial['serial_num']))
print("{:>20}: {:15}".format('Config Register', confreg['confreg_num']))
print(line_div)
