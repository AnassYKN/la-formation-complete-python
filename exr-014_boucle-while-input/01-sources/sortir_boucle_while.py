# Comment peut-on permettre à l'utilisateur de sortir de la boucle
# en modifiant les lignes de code dans la boucle while ?

continuer = "o"
while continuer == "o":
    print("On continue !")
    test = input("Voulez-vous continuer ? o/n ")
    if (test == "o" or test == "Oui" or test == "OUI"):
        break
    else:
        continue
    