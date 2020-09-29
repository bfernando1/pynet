#!/usr/bin/env python3

"""
Author: Bradley Fernando
Purpose: Reads a file and opens it twice. The result of the first output is          a string. The second output results as a list. 

Usage: 
    python exercise1.py

Output: 
    Opening the file...
    
    <file contents> 
    This variable is of type: <class 'str'>
    
    Opening the file again...
    
    <file contents> 
    This variable is of type: <class 'list'>
"""


print("Opening the file...\n")

# Opens the file using .read()
f = open("show_version.txt")
output = f.read()

print(output)
print(f"This variable is of type: {type(output)}\n")
f.close()


print("Opening the file again...\n") 

# Opens the file again using `with` 
with open("show_version.txt") as f:
    output = f.readlines()

print(output)
print(f"\nThis variable is of type: {type(output)}\n")

