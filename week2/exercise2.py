#!/usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Goes through a series of list operations against a list of IPs.  

Usage: 
    python exercise2.py

Output: 
    2.2.2.2
"""


ip_list = ['10.10.10.1',
           '10.10.10.2',
           '10.10.10.3',
           '10.10.10.4',
           '10.10.10.5']

# add a new IP to the list 
ip_list.append('10.10.10.6')           


# add a list to an existing list 
sjc_ips = ['55.55.55.1', '55.55.55.2']
ip_list.extend(sjc_ips) 

# concatinate 2 lists 
sfo_ips = ['44.44.44.3', '44.44.44.4']
ip_list + sfo_ips 

# remove the first element 
ip_list.pop(0)

# remove the last element 
ip_list.pop()

# replace the first ip with 2.2.2.2
ip_list[0] = '2.2.2.2' 

# print the first IP in the list 
print(ip_list[0])
