nombre_mystere = 7
nombre_utilisateur = input("Quel est le nombre mystère ? ")

# Afficher à l'aide d'une structure conditionnelle si le nombre entré par l'utilisateur est plus grand,
# plus petit ou égal au nombre mystère.

if nombre_mystere > int(nombre_utilisateur):
    print("le nombre est plus petit")
elif nombre_mystere < int(nombre_utilisateur):
    print("le nombre est plus grand")
elif nombre_mystere == int(nombre_utilisateur):
    print("le nombre est exacte")