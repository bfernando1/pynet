#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Uses positional and named arguments to call a function that prints the 
         ip address/username/password.

Usage: 
    python exercise-1a.py
Output:
    --------------------------------------------------
    Call function using positional args:
         IP Address: 1.1.1.1
           Username: admin
           Password: cisco
    --------------------------------------------------
    Call function using named args:
         IP Address: 2.2.2.2
           Username: netops
           Password: cisco2
    --------------------------------------------------
    Call functions using positional and named args:
         IP Address: 3.3.3.3
           Username: noc
           Password: cisco3
    --------------------------------------------------
"""

line_div = '-' * 50
def ssh_conn(ip_addr, username, password):
    print("{:>15}: {:20}".format('IP Address', ip_addr))
    print("{:>15}: {:20}".format('Username', username))
    print("{:>15}: {:20}".format('Password', password))
    print(line_div)

print(line_div)
print('Call function using positional args:')
ssh_conn('1.1.1.1', 'admin', 'cisco')

print('Call function using named args:')
ssh_conn(password='cisco2', ip_addr='2.2.2.2', username='netops')

print('Call functions using positional and named args:')
ssh_conn('3.3.3.3', password='cisco3', username='noc')
