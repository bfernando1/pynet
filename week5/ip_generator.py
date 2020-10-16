#! /usr/bin/env python3
"""Generates a random IP address in string format

Usage: 

    python3 ip_generator.py

Output:

    --------------------------------------------------
    Call ip generator with no args:
    10.10.10.68
    --------------------------------------------------
    Call ip generator with positional arg:
    172.16.16.153
    --------------------------------------------------
    Call ip generator with named arg:
    192.168.220.70
    --------------------------------------------------

Author: Bradley Fernando
"""

import random

def ip_gen(prefix_ip='10.10.10.'):
    """Generates the last octet of an IP address
    
    Args:
    	prefix_ip: <string>
                   The first octets seperated by dotted decimals
    
    Returns:
    	The IP address as a string
    
    Examples:
    	>>> ip_gen('1.2.3.')
    	'1.2.3.10'
    
        >>> ip_gen()
        '10.10.10.77'
    """
    return prefix_ip + str(random.randint(1, 254))

line_div = '-' * 50

print(line_div)
print("Call ip generator with no args:")
print((ip_gen()))
print(line_div)

print("Call ip generator with positional arg:")
print(ip_gen('172.16.16.'))
print(line_div)

print("Call ip generator with named arg:")
print(ip_gen(prefix_ip='192.168.220.'))
print(line_div)
