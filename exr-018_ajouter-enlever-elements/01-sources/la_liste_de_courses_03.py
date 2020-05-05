import os
import json
 
dossier_courant = os.path.dirname(__file__)
chemin_liste = os.path.join(dossier_courant, "liste.json")
 
if os.path.exists(chemin_liste):
    with open(chemin_liste, "r") as f:
        liste_de_courses = json.load(f)
else:
    liste_de_courses = []
 
affichage = """
Choisissez une option:
\t1: Ajouter un élément
\t2: Enlever un élément
\t3: Afficher la liste
\t4: Vider la liste
\t5: Terminer
"""
 
option = "0"
 
while option != "5":
    option = input(affichage)
    if(int(option) == 1):
        element = input("Ecrire l'element à ajouter\n")
        liste_de_courses.append(element)
    elif(int(option) == 2):
        element = input("Ecrire l'element à enlever\n")
        if element in liste_de_courses:
            liste_de_courses.remove(element)
        else:
            print("Element not found")
        
    