#! /usr/bin/env python3
"""Use Jinja2 conditionals to print a range of vlans

Usage:
    python3 ex-1c.py

Output:
    vlan 501
      name blue501
    vlan 502
      name blue502
    vlan 503
      name blue503
    vlan 504
      name blue504
    vlan 505
      name blue505
    vlan 506
      name blue506
    vlan 507
      name blue507
    vlan 508
      name blue508

Author: Bradley Fernando
"""
import jinja2

vlan_range = []
for num in range(501, 509):
    vlan_range.append(num)

vlan_vars = {
        "vlan_name": "blue",
        "vlan_num": vlan_range
}

vlan_template = '''
{%- for index in vlan_num %}
vlan {{ index }}
  name {{ vlan_name }}{{ index }}
{%- endfor %}
'''

t = jinja2.Template(vlan_template)
print(t.render(vlan_vars))
