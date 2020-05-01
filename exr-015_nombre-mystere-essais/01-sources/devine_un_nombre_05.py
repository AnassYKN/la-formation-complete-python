import random

nombre_mystere = random.randint(0, 10)

i = 0
is_win = False
while(i < 5):
    nombre = input("Quel est le nombre mystère ? ")
    if not nombre.isdigit():
        print("SVP, entrez un nombre valide.")
        i += 1
        continue

    nombre = int(nombre)
    if nombre > nombre_mystere:
        print(f"Le nombre mystère est plus petit que {nombre}")
        print(f"Nombre essaie:{i+1}")
        i += 1
        continue
    elif nombre < nombre_mystere:
        print(f"Le nombre mystère est plus grand que {nombre}")
        print(f"Nombre essaie:{i+1}")
        i += 1
        continue
    else:
        print("Bravo, vous avez trouvé le nombre mystère !")
        is_win=True
        break

if(is_win == False):
    print(f"vous avez perdu le nombre mystère {nombre_mystere}")
    

