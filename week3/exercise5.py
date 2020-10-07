#! /usr/bin/env python3
"""
Author: Bradley Fernando
Purpose: Generates a range of IPs for 10.0.0.0/24 and prints it to standard
         output. Takes a section of the list and performs a ping on an OS level. 
         
Usage: 
    python exercise4.py

Output: 
    0 ---> 10.0.0.1
    1 ---> 10.0.0.2
    2 ---> 10.0.0.3
    3 ---> 10.0.0.4
    4 ---> 10.0.0.5
    5 ---> 10.0.0.6
    ...

    <snipped>

    252 ---> 10.0.0.253
    253 ---> 10.0.0.254
    
    --------------------------------------------------------------------------------
    PING 10.0.0.3 (10.0.0.3): 56 data bytes
    64 bytes from 10.0.0.3: icmp_seq=0 ttl=255 time=3.086 ms
    64 bytes from 10.0.0.3: icmp_seq=1 ttl=255 time=9.798 ms
    
    --- 10.0.0.3 ping statistics ---
    2 packets transmitted, 2 packets received, 0.0% packet loss
    round-trip min/avg/max/stddev = 3.086/6.442/9.798/3.356 ms
    PING 10.0.0.4 (10.0.0.4): 56 data bytes
    Request timeout for icmp_seq 0
    ...

    <snipped>
"""
import os
WINDOWS = False

# Generate a list of usable IPs in 10.0.0.0/24
ip_list = []
for ip in range(1, 255):
    ip_list.append("10.0.0." + str(ip))

# Display the enumerated IPs 
for count, ip in enumerate(ip_list):
    print(f"{count} ---> {ip}")

base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

short_list = ip_list[2:6]
line_divider = '-' * 80

# Ping a shortened list of IPs
print(f"\n{line_divider}")

for ping in short_list:
    os.system(f"{base_cmd} {ping}")

print(f"\n{line_divider}")
