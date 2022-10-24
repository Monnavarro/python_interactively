# -- coding: utf-8 --
"""

Created on: 22/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
empty_list = []
empty_tuple = ()
empty_string = ""
nothing = None


if empty_list == []:
    print("It's an empty list!")
if empty_tuple == ():
    print("It's an empty tuple!")
if empty_string == "":
    print("It's an empty String!")


empty_string = "something"
if empty_string == "":
    print("This is an empty string!") # No regreesa nada

# Comparaciones
empty_list = []
empty_string = "something"
nothing = None

print(empty_list == empty_string) # False
print(empty_string == nothing) # False
