#! /usr/bin/env python3
import re 

def format_mac(mac_string):
    """Takes a raw string and contructs a formatted mac address

    Args: 
        mac_string: <string>

    Returns:
        string 
    """
    # Check for potential delimiters 
    mac_string = re.split(r"[.\-/:]", mac_string)

    # Add padding for single value octets
    mac_addr = octet_check(mac_string)
     
    mac_addr = ''.join(mac_string)

    mac_list = []
    # Delimit a ':' every 2 hexidecimals
    while len(mac_addr) > 0:
        new_mac = mac_addr[:2]
        mac_addr = mac_addr[2:]
        mac_list.append(new_mac)

    return ':'.join(mac_list).upper()


def octet_check(octet):
    """Takes a list and checks the length of each index
    
    Args:
        octet: <list> 

    Returns:
        octet: <list>
    """
    for num, hex_val in enumerate(octet):
        if len(octet[num]) == 4:
            continue
        elif len(octet[num]) != 2: 
            octet[num] = '0' + octet[num]
    return octet

# Validate with tests
assert "AA:BB:CC:DD:EE:FF" == format_mac("aabb.ccdd.eeff")
assert "0A:0B:0C:0D:0E:0F" == format_mac("a:b:c:d:e:f")
assert "01:02:0A:0B:03:44" == format_mac("1:2:a:b:3:44")
assert "0A:0B:0C:0D:0E:0F" == format_mac("a-b-c-d-e-f")
assert "01:02:0A:0B:03:44" == format_mac("1-2-a-b-3-44")
assert "01:23:02:34:04:56" == format_mac("123.234.456")

