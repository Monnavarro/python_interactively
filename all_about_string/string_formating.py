# -- coding: utf-8 --
"""

Created on: 21/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
my_string = "I like %s" % "Python"
print(my_string)

var = "cookies"
newString = "I like %s" % var
print(newString)  # I like cookies

another_string = "I like %s and %s" % ("Python", var)
print(another_string)  # I like Python and cookies

another_string = "I like %s and %s" % "Python"


my_string = "%i + %i = %i" % (1, 2, 3)
print(my_string) # '1 + 2 = 3'

float_string = "%f" % (1.23)
print(float_string) # '1.230000'

float_string2 = "%.2f" % (1.23)
print(float_string2) # '1.23'

float_string3 = "%.2f" % (1.237)
print(float_string3) # '1.24'









