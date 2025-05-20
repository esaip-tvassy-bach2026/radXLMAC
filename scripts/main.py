"""
Ce fichier contient le code principal du programme. Il permet de lancer le menu principal.
"""
exemple_de_nom_de_fichier="ma_superbe_archive.xlsx"

def menu_launch():
    """
    Cette fonction permet de lancer et démarrer l-application.
    """
    print("\n===== radXLMAC - MENU PRINCIPAL =====")
    print("This program was made by Thomas VASSY--ROUSSEAU, intern at TIMCOD OUEST in May 2025. More informations about him at https://github.com/esaip-tvassy-bach2026.")
    print("Copyright (C) TIMCOD SAS, 2025-2030. All rights reserved.")
    print("Copyright (C) TIMCOD OUEST SAS, 2025-2030. All rights reserved.")
    print("Chargement terminé avec succès.")
    print("\nINFORMATIONS IMPORTANTES")
    print(" + Votre fichier doit être obligatoirement au format XSLX pour pouvoir être traité. Ce programme ne fonctionne pas avec d-autres formats.")
    print(" + Ne pas mettre de chemins d-accès en réponse aux questions qui vous seront demandées.")
    print(" + Le fichier XLSX à traiter doit être exactement dans le même dossier que le fichier main.py.")
    print(" + L-ensemble des adresses MAC physiques doivent déjà être renseignées dans votre fichier Excel et le fichier doit être bien enregistré.")
    print(" + Pensez à enregistrer votre travail et à fermer Excel avant de lancer ce programme. Il est possible qu-Excel plante ou que vous ayez des messages d-erreur si vous exécutez les deux programmes en même temps.")
    print(" + Le fichier XLSX doit impérativement être nommé avec des underscores (_) pour les espaces et des lettres minuscules. Python déteste les accents, les espaces et les caractères spéciaux (sauf _) dans les noms de fichiers.")
    print(f" + Exemple de nom de fichier correct : {exemple_de_nom_de_fichier}.")
    confirmation_de_lancement=str(input("Tapez O si vous êtes prêt à continuer. Dans le cas contraire, tapez N."))
    while confirmation_de_lancement!="O" and confirmation_de_lancement!="N":
        print("Vous avez fait une erreur de saisie. Veuillez réessayer (faites attention aux majuscules, le système est sensible à la casse).")
        confirmation_de_lancement=str(input("Tapez O si vous êtes prêt à continuer. Dans le cas contraire, tapez N."))
    if confirmation_de_lancement=="N":
        quit()
    menu_principal(confirmation_de_lancement)

def menu_principal(confirm):
    """
    Ceci est le menu principal de l-application.
    """
    assert isinstance(confirm,str), "Vous avez dû faire une erreur de saisie dans le programe. Le programme s-arrête ici."
    assert confirm=="O", "Erreur. Vous avez demandé l-arrêt du programme, donc le programme s-arrête."
    print("\nIMPORTANT : VOUS ALLEZ SAISIR DES INFORMATIONS QUE VOUS NE POURREZ PAS MODIFIER PAR LA SUITE.")
    print(f"\nMerci d-indiquer le nom exact du fichier, y compris son extansion. Par exemple : {exemple_de_nom_de_fichier}.")
    nom_du_fichier=str(input("Quel est le nom du fichier XLSX que je dois utiliser pour calculer et rentrer les adresses MAC ?"))
    print("\n")
    nom_de_la_feuille=str(input("Quel est le nom exact de la feuille à modifier dans votre fichier Excel ?"))
    print("\n")
    nom_colonne_MAC_B=str(input("Quel est le nom exact de la colonne du tableau où sont écrites les adresses MAC physiques des points d-accès Wi-Fi ?"))