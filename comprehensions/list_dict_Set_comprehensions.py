# -- coding: utf-8 --
"""

Created on: 24/10/22
@author: Montse Navarro <montserrat.nvro.lpz@gmail.com>
Licence,
"""
# iterando un for

x = [i for i in range(5)]
print(x)


line = ['SOME TERM', 'AMIG', 'some term', 'Some Term']
phrase = "SOME TERM"

if [i for i in line if phrase in i]:
    print('La frase {} aparace en la lita'.format(phrase))
else:
    print('La frase {}  NO aparace en la lita'.format(phrase))

Z = [i for i in line if phrase in i]
print(Z)

# quitando espacios
myStringList = [
  '    Hello how are you?',
  'I\'m good    ',
  '    I\'m good too   ']

myString = [word.strip() for word in myStringList]
print(myString)

#lista anidada
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
juntar_vec = [num for elemento in vec for num in elemento]
print(juntar_vec)


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for elem in vec:
    for num in elem:
        print(num)


vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
union_vec = []
for elem in vec:
    for num in elem:
        union_vec.append(num)
print(union_vec)

ejemplo_dict = {'a': 1, 'b': 2}
ejemplo = [x for x in ejemplo_dict.keys()]


# Dictoniary comprehensions
print({i: str(i) for i in range(5)})

#forma larga
reco = {}
for i in range(5):
    reco.update({i: str(i)})
print(reco)

dictionary = {'A': 1, 'B': 2, 'C': 3}
key, value = 'D', 4
dictionary[key] = value


my_dict = {1: "dog", 2: "cat", 3: "hamster"}
print({value: key for key, value in my_dict.items()})

#Conjuntos
my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = set(my_list)
print(my_set) # {1, 2, 3, 4, 5, 7, 8}
type(my_set)


my_list = [1, 2, 2, 3, 4, 5, 5, 7, 8]
my_set = {x for x in my_list}
print(my_set) # {1, 2, 3, 4, 5, 7, 8}







