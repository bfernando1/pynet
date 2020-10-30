#! /usr/bin/env python3
import yaml
import jinja2

from pprint import pprint

with open("intf.yml") as f:
    output = yaml.load(f, Loader=yaml.Loader)

# Dictionary of all interfaces
if_dict = output['interfaces']


def if_parse(interface):
    """Function that creates a generic dictionary for a single interface"""
    access_vlan_ = None
    native_vlan_ = None
    trunk_vlans_ = None

    switchport_mode_ = if_dict[interface]['mode']
    if switchport_mode_ == 'access':
        access_vlan_ = if_dict[interface]['vlan']
    elif switchport_mode_ == 'trunk':
        native_vlan_ = if_dict[interface]['native_vlan']
        trunk_vlans_ = if_dict[interface]['trunk_vlan']
    
    if_out = {
            "interface_name": interface,
            "switchport_mode": switchport_mode_,
            "access_vlan": access_vlan_,
            "native_vlan": native_vlan_,
            "trunk_vlans": trunk_vlans_
    }
    return if_out
    

# Write jinja template for each interface
for k,v in if_dict.items():
    intf_vars = if_parse(k) 

    with open("intf.j2") as f:
        output = f.read()
    t = jinja2.Template(output)

    print(t.render(intf_vars))
