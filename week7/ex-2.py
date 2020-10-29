#! /usr/bin/env python3
"""Uses an external Jinja2 template to generate OSPF configs

Usage:
    python3 ex-2.py

Output:
    --------------------------------------------------
    interface vlan 1
      ip ospf priority 100
    router ospf 10
      passive-interface default
      no passive-interface Vlan1
      no passive-interface Vlan2
      network 10.10.10.0/24 area 0.0.0.0
      network 10.10.20.0/24 area 0.0.0.0
      network 10.10.30.0/24 area 0.0.0.0
      max-lsa 12000
    --------------------------------------------------

Author: Bradley Fernando
"""
import jinja2

ospf_nets = [
        "10.10.10.0/24", 
        "10.10.20.0/24", 
        "10.10.30.0/24"
]
ospf_intfs = ["Vlan1", "Vlan2"]

ospf_vars = {
        "ospf_priority": 100,
        "ospf_process_id": 10,
        "ospf_active_interfaces": ospf_intfs,
        "ospf_area0_networks": ospf_nets
}


line_div = '-' * 50

with open("ospf_template.j2") as f:
    output = f.read()
t = jinja2.Template(output)

print(line_div)
print(t.render(ospf_vars))
print(line_div)
