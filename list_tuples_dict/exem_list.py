# -- coding: utf-8 --
"""

Created on: 22/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
my_list = []
my_list= list()

my_list1 = [1, 2, 3]
my_list2 = ["a", "b", "c"]
my_list3 = ["a", 1, "python", 5]

print(my_list, my_list1, my_list2, my_list3)
# [] [1, 2, 3] ['a', 'b', 'c'] ['a', 1, 'python', 5]

#Listas anidadas:
my_list_needed = [my_list, my_list1, my_list2, my_list3]
# [[], [1, 2, 3], ['a', 'b', 'c'], ['a', 1, 'python', 5]]

# Combinando dos listas:
comb_list = []
comb_list.extend(my_list3)
print(comb_list)

comb_list2 = my_list1 + my_list2
print(comb_list2)

# Ordenando listas
alpha_list = [34,38,20,40,10]
alpha_list.sort()
print(alpha_list)  # [10, 20, 34, 38, 40]

# asignado el orden a una variable
alpha_list = [34, 23, 67, 100, 88, 2]
sorted_list = alpha_list.sort()
print(sorted_list) #  None  --> NO SE PUEDE ASIGNAR A OTRA VARIABLE
""" el ordenamiento de una lista, solo se puede ordenar en la misma 
lista desordenada."""


# SLICING de listas
alpha_list = [34, 23, 67, 100, 88, 2]
alpha_list.sort()
print(alpha_list[:3]) # [2, 23, 34]



