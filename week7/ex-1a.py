#! /usr/bin/env python3
"""Uses Jinja2 templating to print a vlan description

Usage:
    python3 ex-1a.py

Output:
    vlan 400
      name red400

Author: Bradley Fernando
"""
import jinja2

vlan_vars = {
        "vlan_name": "red400",
        "vlan_num": 400
}

vlan_template = '''
vlan {{ vlan_num }}
  name {{ vlan_name }}
'''

t = jinja2.Template(vlan_template)
print(t.render(vlan_vars))

