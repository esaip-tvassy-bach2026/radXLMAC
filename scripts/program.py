"""
Ce fichier contient le cerveau du programme. C-est le fichier central du programme.
"""
from calculer import calcul

def lancement_programme(forme,filename,sheet,MAC_B,nbr_rad,MAC_rad):
    """
    Cette fonction permet de vérifier les informations entrées et de lancer les calculs.
    Entrée : forme(str), filename(str), sheet(str), MAC_B(str), nbr_rad(int), MAC_rad(str).
    Sortie : lancement des calculs et enregistrement du nouveau fichier Excel.
    """
    assert isinstance(forme,str) and isinstance(filename,str), and isinstance(sheet,str) and isinstance(MAC_B,str) and isinstance(nbr_rad,int) and isinstance(MAC_rad,str), "ERREUR FATALE : Les données entrées ne sont pas dans les bons formats. Veuillez vérifier que vous avez entré que des chaînes de caractères et des nombres entiers. Le programme doit s-arrêter ici."
    assert forme=="O" or forme=="N", "ERREUR FATALE : Vous n-avez pas ou avez mal précisé si vous souhaitiez que le programme formatte les adresses MAC ou non. Relancez tout et corrigez votre saisie. Le programme doit s-arrêter ici."
    assert "xlsx" in filename, "ERREUR FATALE : Le fichier que vous avez indiqué n-a pas l-extension .xlsx. Veuillez relancer le programme puis corriger votre saisie. Le programme doit s-arrêter ici."