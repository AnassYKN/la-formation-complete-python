"""
Dans cet exercice vous devez afficher les lettres du mot 'Python' dans le sens inverse.
Votre script devra donc afficher :
n
o
h
t
y
P
"""

import pprint as p
python = list("Pyhton")
nothyp = []
for i in python:
    nothyp.append(python[len(python) - python.index(i)-1])
print(*nothyp, sep = "\n") 



