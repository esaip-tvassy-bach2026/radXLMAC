"""
Ce fichier contient le code permettant de charger des fichiers XLSX.
"""
import pandas

def charger(fichier,feuille_de_calcul):
    """
    Cette fonction charge un fichier XLSX et retourne le contenu d-une de ses feuilles.
    Ce fichier utilise la libraire pandas de Python.
    Entrée : fichier(str), feuille_de_calcul(str)
    Sortie : Retourne le contenu de la feuille via la libraire pandas.
    """
    assert isinstance(fichier,str) and isinstance(feuille_de_calcul,str), "ERREUR FATALE : Les paramètres donnés à la fonction charger ne sont pas dans les bons formats. Veuillez relancer le programme entièrement et corriger votre saisie. Le programme doit s-arrêter ici."
    assert "xlsx" in fichier, "ERREUR FATALE : Vous semblez ne pas utiliser un fichier au format XLSX. Veuillez relancer totalement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
    contenu_final=pandas.read_excel(fichier,sheet_name=feuille_de_calcul)
    return contenu_final

print("ERREUR FATALE : Vous ne pouvez pas lancer ce script seul (mode standalone).")
print("Veuillez lancer le programme en entier en exécutant le script main.py.")
print("\nPython doit s-arrêter ici.")
quit()