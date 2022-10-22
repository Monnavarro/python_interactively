# -- coding: utf-8 --
"""

Created on: 22/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
my_dict = {}

another_dict = dict()

my_other_dictionary = {"one": 1, "two": 2, "three": 3}
print(my_other_dictionary)

# Accediendo a VALOR de un diccionario
print(my_other_dictionary["two"]) # 2

for item in my_other_dictionary:
    valores = my_other_dictionary[item]

    print(valores)

## Retornando valores de un diccionario
my_dict = {"name": "Mike", "address": "123 Happy Way", "sex": "muscle"}

for key in my_dict:
    value = my_dict[key]
    print(value)

#Para ver si una key esta definida en el diccionario:
my_dict = {"name": "Mike", "address": "123 Happy Way", "sex": "muscle"}

print("name" in my_dict) # True
print("telephone" in my_dict) # False
print("name" in my_dict.keys()) # True

# if you need to get a list of all keys in a dictionary:
my_dict = {"name": "Mike", "address": "123 Happy Way", "sex": "muscle"}
keys_my_dict = my_dict.keys()
print(keys_my_dict)



