#! /usr/bin/env python3
"""Uses Jinja2 templating to output the ISAKMP configs
Usage:
    python ex-1b.py

Output: 
    cryptp isakmp policy 10
      encr aes
      authentication pre-share
      group 5
    crypto isakmp key my_key address no-xauth
    crypto isakmp keepalive 10 periodic

Author: Bradley Fernando
"""
import jinja2

isakmp_vars = {
        "isakmp_enable": True,
        "encryption": "aes",
        "dh_group": 5,
        "auth": "pre-share",
        "psk": "my_key"
}

isakmp_template = '''
{%- if isakmp_enable %}
cryptp isakmp policy 10
  encr {{ encryption }}
  authentication {{ auth }}
  group {{ dh_group }}
crypto isakmp key {{ psk }} address no-xauth 
crypto isakmp keepalive 10 periodic
{%- endif %}
'''

t = jinja2.Template(isakmp_template)
print(t.render(isakmp_vars))

