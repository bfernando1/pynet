#! /usr/bin/env python3
"""Takes yaml as input and generates a interface config using jinja2 templating

Usage:
    python3 ex-4.yml

Output:
    interface Ethernet1
      switchport mode access
      switchport access vlan 10
    interface Ethernet2
      switchport mode access
      switchport access vlan 20
    interface Ethernet3
      switchport mode trunk
      switchport trunk native vlan 1
      switchport trunk allowed vlan al

Author: Bradley Fernando
"""
import yaml
import jinja2

from pprint import pprint

with open("intf.yml") as f:
    intf_vars = yaml.load(f, Loader=yaml.Loader)
    
with open("intf.j2") as f:
    output = f.read()
t = jinja2.Template(output)

print(t.render(intf_vars))
