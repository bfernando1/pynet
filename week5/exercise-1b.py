#! /usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Calls a ssh connection function using keyword args (kwargs) and default
         args. 

Usage: 
    python exercise-1b.py
Output:

    --------------------------------------------------
    Display the device type using the default arg
         IP Address: 3.3.3.3
           Username: noc
           Password: cisco3
        Device Type: cisco_ios
    --------------------------------------------------
    Display the device type using the specified arg
         IP Address: 3.3.3.3
           Username: noc
           Password: cisco3
        Device Type: juniper_junos
    --------------------------------------------------
    Supply function using a dictionary and kwargs
         IP Address: 172.16.30.24
           Username: devnet
           Password: cisco123
        Device Type: nxos
    --------------------------------------------------
"""
line_div = '-' * 50

def ssh_conn(ip_addr, username, password, device_type='cisco_ios'):
    print("{:>15}: {:20}".format('IP Address', ip_addr))
    print("{:>15}: {:20}".format('Username', username))
    print("{:>15}: {:20}".format('Password', password))
    print("{:>15}: {:20}".format('Device Type', device_type))
    print(line_div)

print(line_div)
print('Display the device type using the default arg')
ssh_conn('3.3.3.3', password='cisco3', username='noc')

print('Display the device type using the specified arg')
ssh_conn('3.3.3.3', password='cisco3', username='noc',
        device_type='juniper_junos')

net_mgmt = {'ip_addr': '172.16.30.24',
            'username': 'devnet',
            'password': 'cisco123',
            'device_type': 'nxos'
}

print('Supply function using a dictionary and kwargs')
ssh_conn(**net_mgmt)
