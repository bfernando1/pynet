#! /usr/bin/env python3
"""Reads in a list in yaml and prints to standard output

Usage: 
    python3 ex-3b.yml

Output:

Author: Bradley Fernando
"""
import yaml
from pprint import pprint

with open("intf-3b.yml") as f:
    output = yaml.load(f, Loader=yaml.Loader)
        
pprint(output)
