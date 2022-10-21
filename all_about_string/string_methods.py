# -- coding: utf-8 --
"""

Created on: 20/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
my_string = "This is string!"
print(my_string.upper())

# list of all the string methods
print(dir(my_string))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__',
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
#  '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__',
#  '__rmul__','__setattr__', '__sizeof__', '__str__', '__subclasshook__',
#  'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith',
#  'expandtabs', 'find','format', 'format_map', 'index', 'isalnum',
#  'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier',
#  'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper',
#  'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace',
#  'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split',
# 'splitlines', 'startswith',  'strip', 'swapcase', 'title',
# 'translate', 'upper', 'zfill']

# Para ver que hace cada metódo
print(help(my_string.title))

# Para saber que tipo de dato es:
print(type(my_string))



