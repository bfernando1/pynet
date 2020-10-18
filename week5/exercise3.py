#! /usr/bin/env python3

def format_mac(mac_string):
    if '.' in mac_string:
        delimiter = '.'
    elif '-' in mac_string:
        delimiter = '-'
    elif ':' in mac_string:
        delimiter = ':'
    mac_string = mac_string.upper().split(delimiter)
    mac_addr = octet_check(mac_string)

    mac_addr = ''.join(mac_string)

    mac_list = []
    while len(mac_addr) > 0:
        new_mac = mac_addr[:2]
        mac_addr = mac_addr[2:]
        mac_list.append(new_mac)

    return ':'.join(mac_list)


def octet_check(octet):
    for num, hex_val in enumerate(octet):
        if len(octet[num]) == 4:
            continue
        elif len(octet[num]) != 2: 
            octet[num] = '0' + octet[num]
    return octet
        
   
#print(format_mac('aaaa.bbbb.cccc'))
#print(format_mac('aa-aa-bb-bb-cc-cc'))
#print(format_mac('a:b:c:d:e:f'))
#print(format_mac('aa:bb:cc:d:e:f'))
#print(format_mac('aa.bbb.cccc'))

assert "AA:BB:CC:DD:EE:FF" == format_mac("aabb.ccdd.eeff")
assert "0A:0B:0C:0D:0E:0F" == format_mac("a:b:c:d:e:f")
assert "01:02:0A:0B:03:44" == format_mac("1:2:a:b:3:44")
assert "0A:0B:0C:0D:0E:0F" == format_mac("a-b-c-d-e-f")
assert "01:02:0A:0B:03:44" == format_mac("1-2-a-b-3-44")
assert "01:23:02:34:04:56" == format_mac("123.234.456")
print(format_mac("aabb.ccdd.eeff"))
print(format_mac("123.234.456"))
