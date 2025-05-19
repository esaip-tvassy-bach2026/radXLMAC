"""
Ce fichier contient le code principal du programme. Il permet de lancer le menu principal.
"""

def menu_launch():
    print("\n==== radXLMAC - MENU PRINCIPAL ====")
    print("Copyright (C) TIMCOD SAS, 2025-2030. All rights reserved.")
    print("Copyright (C) TIMCOD OUEST SAS, 2025-2030. All rights reserved.")
    print("Copyright (C) Thomas VASSY--ROUSSEAU, 2025-2027. All rights reserved.")
    print("Chargement terminé avec succès.")
    print("\nINFORMATIONS IMPORTANTES")
    print(" + Votre fichier doit être obligatoirement au format XSLX pour pouvoir être traité. Ce programme ne fonctionne pas avec d'autres formats.")
    print(" + Ne pas mettre de chemins d'accès en réponse aux questions qui vous seront demandées.")
    print(" + Le fichier XLSX à traiter doit être exactement dans le même dossier que le fichier main.py.")
    confirmation_de_lancement=input("Tapez O si vous êtes prêt à continuer. Dans le cas contraire, tapez N.")
    while confirmation_de_lancement!="O" or confirmation_de_lancement!="N":
        print("Vous avez fait une erreur de saisie. Veuillez réessayer (faites attention aux majuscules, le système est sensible à la casse).")
        confirmation_de_lancement=str(input("Tapez O si vous êtes prêt à continuer. Dans le cas contraire, tapez N."))
    menu_principal(confirmation_de_lancement)

def menu_principal(confirm="N"):
    """
    Ceci est le menu principal de l'application.
    """
    assert isinstance(confirm,str) and (confirm=="O" or confirm=="N"), "Vous avez dû faire une erreur de saisie dans le programe. Le programme s'arrête ici."
    if confirm=="N":
        quit()
    print("\nIMPORTANT : VOUS ALLEZ SAISIR DES INFORMATIONS QUE VOUS NE POURREZ PAS MODIFIER PAR LA SUITE.")
    nom_du_fichier=str(input("Quel est le nom du fichier XLSX que je dois utiliser pour calculer et rentrer les adresses MAC ?"))