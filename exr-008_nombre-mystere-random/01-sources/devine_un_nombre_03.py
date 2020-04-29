import random
#  Remplacer le nombre mystère par un nombre aléatoire
a = random.randrange(99)
b = random.randrange(99)


if b > a:
    print("Le nombre b est plus grand que le nombre a.")
elif a > b:
    print("Le nombre a est plus grand que le nombre b.")
else: 
    print("Le nombre a et b sont égaux.")