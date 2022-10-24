# -- coding: utf-8 --
"""

Created on: 22/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
x = 10
y = 20

if x < 10 or y > 15:
    print("This statement was True!")
######
x = 10
y = 10
if x == 10 and y == 15:
    print("This statement was True")
else:
    print("The statement was False!")
#####
my_list = [1, 2, 3, 4]
x = 10
if x not in my_list:
    print("'x' is not in the list, so this is True!")
#######
x = 10
if x != 11:
    print("x is not equal to 11!")
#####
my_list = [1, 2, 3, 4]
x = 10
z = 11
if x not in my_list and z != 10:
    print("This is True!")

