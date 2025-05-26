"""
Ce fichier contient la commande permettant de copier des fichiers.
"""
import shutil

def copie(fichier,nom_destination):
    """
    Cette fonction permet de copier des fichiers.
    Entrée : fichier(str), nom_destination(str)
    Sortie : Pas de sortie, le fichier est copié et collé avec son nouveau nom.
    """
    assert isinstance(fichier,str) and isinstance(nom_destination,str), "ERREUR FATALE : Il semble que vous avez une erreur de format dans le nom de votre archive initiale ou dans le nom de votre archive de destination. Veuillez fermer, redémarrer le programme et corriger votre saisie. Le programme doit s-arrêter ici."
    assert "xlsx" in fichier, "ERREUR FATALE : Il semble que vous essayez d-utiliser cette fonction avec un fichier qui n-a pas l-extension XLSX. Ceci est impossible et n-est pas supporté par ce programme. Veuillez arrêter et redémarrer le programme afin de corriger votre saisie. Le programme doit s-arrêter ici."
    assert "xlsx" in nom_destination, "ERREUR FATALE : Il semble que vous essayez d-utiliser cette fonction avec un fichier de destination qui n-a pas l-extension XLSX. Ceci est impossible et n-est pas supporté par ce programme. Veuillez arrêter et redémarrer le programme afin de corriger votre saisie. Le programme doit s-arrêter ici."
    shutil.copy(fichier,nom_destination)