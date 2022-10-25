# -- coding: utf-8 --
"""

Created on: 25/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# ejecutando esto arroja un error:
1/0

#para solventarlo:
try:
    1/0
except ZeroDivisionError:
    print("You cannot divide by zero!")

#Accediendo a la clave de un dict que no existe
my_dict = {"a":1, "b":2, "c":3}
try:
    value = my_dict["d"]
except KeyError:
    print("The key does not exist")

#Accediendo a un elemento de lista que no existe
my_list = [1, 2, 3, 4, 5]
try:
    my_list[6]
except IndexError:
    print("That index is not in the list")


#multiples exceptions
my_dict = {"a": 1, "b": 2, "c": 3}
try:
    values = my_dict["d"]
except IndexError:
    print("The Index does not exist")
except KeyError:
    print("This key is not in the dictionary!")
except:
    print("Some other error occurred!")
finally:
    print("The finally statement has executed!")

# try, except, else
my_dict = {"a":1, "b":2, "c":3}

try:
    value = my_dict["a"]
except KeyError:
    print("This key is not in the dictionary!")
else:
    print("No error occurred!, the value is: {}". format(value))





