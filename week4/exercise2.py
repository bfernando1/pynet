#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Takes a list from 3 data centers and performs set operations against
         them. 
        

Usage: 
    python exercise2.py

Output:

    Houston DC:
    ------------------------------
         172.16.5.2
          10.23.5.2
         172.16.5.3
          10.23.5.1
          10.23.5.6
          10.23.5.3
          10.23.5.4
    
    Atlanta DC:
    ------------------------------
         172.16.5.6
         172.16.6.3
         172.16.5.2
         172.16.6.4
         172.16.5.3
         172.16.6.5
         172.16.6.2
         172.16.6.1
    
    Chicago DC:
    ------------------------------
         172.16.5.6
         172.16.5.2
         172.16.5.3
         172.16.6.5
        192.168.7.1
        192.168.7.2
        192.168.7.4
        192.168.7.3
    
    Common IPs between Houston and Atlanta
    ------------------------------
    {'172.16.5.3', '172.16.5.2'}
    
    Common IPs between Houston, Atlanta, and Chicago
    ------------------------------
    {'172.16.5.3', '172.16.5.2'}
    
    IP's unique to Chicago
    ------------------------------
    {'192.168.7.2', '192.168.7.1', '192.168.7.4', '192.168.7.3'}
"""

houston_dc = ['10.23.5.1', '10.23.5.2', '10.23.5.3', '10.23.5.4', \
              '10.23.5.1', '172.16.5.2', '172.16.5.3', '10.23.5.4',\
              '10.23.5.3', '10.23.5.6'
]

atlanta_dc = ['172.16.6.1', '172.16.6.2', '172.16.6.3', '172.16.6.4', \
              '172.16.5.2', '172.16.5.3', '172.16.6.5', '172.16.5.6'
]


chicago_dc = ['192.168.7.1', '192.168.7.2', '192.168.7.3', '192.168.7.4', \
              '172.16.5.2', '172.16.5.3', '172.16.6.5', '172.16.5.6'
]

set_houston = set(houston_dc)
set_atlanta = set(atlanta_dc)
set_chicago = set(chicago_dc)

line_div = '-' * 30

# Print Houston IPs
print()
print('Houston DC:')
print(line_div)
for ip in set_houston:
    print(f"{ip:>15}")
print()

# Print Atlanta IPs
print('Atlanta DC:')
print(line_div)
for ip in set_atlanta:
    print(f"{ip:>15}")
print()

# Print Chicago IPs
print('Chicago DC:')
print(line_div)
for ip in set_chicago:
    print(f"{ip:>15}")
print()


print("Common IPs between Houston and Atlanta")
print(line_div)
print(set_houston.intersection(set_atlanta))
print()

print("Common IPs between Houston, Atlanta, and Chicago")
print(line_div)
print(set_houston & set_chicago)
print()

print("IP's unique to Chicago")
print(line_div)
print(set_chicago - set_atlanta - set_houston)

