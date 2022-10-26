# -- coding: utf-8 --
"""

Created on: 25/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
path = "/Users/mon/projects/python_interactively/working_with_files/"

handle = open(path + "test.txt", "r")


def get_read_lines():
    for line in handle:
        return line

    handle.close()

