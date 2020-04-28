nombre_mystere = 7

# Demander à l'utilisateur de deviner le nombre.
# Afficher si le nombre entré par l'utilisateur est égal au nombre mystère.

a = input("Entrez le nombre mystere \n")
resultat = f"resultat : {int(a) == int(nombre_mystere)}"
print(resultat)
