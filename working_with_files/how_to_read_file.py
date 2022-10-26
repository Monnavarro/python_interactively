# -- coding: utf-8 --
"""

Created on: 25/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
import os

# leer un archivo de texto:
handle = open("test.txt") # arroja error porque
#no estas en la ruta del archivo de texto para acceder a el.

# ruta actual
print(os.path.abspath(os.getcwd())) # /Users/mon/projects/python_interactively

# Accediendo a la ruta del archivo
path = (os.path.abspath(os.getcwd()) + "/working_with_files/")
print(path)

# Acceder al archivo de texto
handle = open(path + "test.txt", "r")
data = handle.read()
print(data)
handle.close() # es importante cerrar siempre el archivo.

# Para leer solo una línea del archivo:
handle = open(path + "test.txt", "r")
data = handle.readline()
print(data)
handle.close()

# readlines es una LISTA
handle = open(path + "test.txt", "r")
data = handle.readlines()
print(data)
handle.close()


