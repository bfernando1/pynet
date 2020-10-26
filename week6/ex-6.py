#! /usr/bin/env python3
""" Connects to multiple devices through Netmiko and outputs
    a 'show version' in structured data

Usage:
    python3 ex-6.py

Output:
    --------------------------------------------------
    Running command: show version on cisco_ios
    --------------------------------------------------
    [{'config_register': '0x2102',
      'hardware': ['881'],
      'hostname': 'cisco1',
      'mac': [],
      'reload_reason': 'Reload Command',
      'rommon': 'System',
      'running_image': 'c880data-universalk9-mz.155-3.M8.bin',
      'serial': ['FTX1512038X'],
      'uptime': '26 weeks, 6 days, 8 hours, 3 minutes',
      'version': '15.5(3)M8'}]
    --------------------------------------------------
    Running command: show version on cisco_nxos
    --------------------------------------------------
    [{'boot_image': 'bootflash:///nxos.9.2.3.bin',
      'hostname': 'nxos1',
      'last_reboot_reason': 'Unknown',
      'os': '9.2(3)',
      'platform': '9000v',
      'uptime': '69 day(s), 12 hour(s), 50 minute(s), 52 second(s)'}]
    --------------------------------------------------
    Running command: show version on juniper_junos
    --------------------------------------------------
    [{'appid_services': '',
      'base_os_boot': '',
      'base_os_software_suite': '',
      'border_gateway_function_package': '',
      'crypto_software_suite': '',
      'hostname': 'srx1',
      'idp_services': '',
      'junos_version': ''
    <!--snipped-->

Author: Bradley Fernando
"""

from netmiko import Netmiko
from getpass import getpass
from pprint import pprint

password = getpass()

cisco1 = {
    "device_type": "cisco_ios",
    "host": "cisco1.lasthop.io",
    "username": "pyclass",
    "password": password
}

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password
}

srx1 = {
    "device_type": "juniper_junos",
    "host": "srx1.lasthop.io",
    "username": "pyclass",
    "password": password
}

# Command that Netmiko will run
command = 'show version'
line_div = '-' * 50

for devices in [cisco1, nxos1, srx1]:
    with Netmiko(**devices) as net_connect:
        output = net_connect.send_command(command, use_textfsm=True)
        net_connect.disconnect()
    print(line_div)
    print(f"Running command: {command} on {devices['device_type']}")
    print(line_div)
    pprint(output)

print(line_div)
