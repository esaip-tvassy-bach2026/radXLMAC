"""
Ce fichier contient le code permettant de charger des fichiers XLSX.
"""
from openpyxl import load_workbook

def charger(fichier,feuille):
	"""
	Cette fonction permet de charger une feuille particulière dans un fichier XLSX.
	Entrée : fichier(str), feuille(str)
	Sortie : workbook (contient tous les éléments du classeur XLSX), worksheet (contient tous les éléments de la feuille de travail)
	"""
	assert isinstance(fichier,str) and isinstance(feuille,str), "ERREUR FATALE : Il semble que votre nom de fichier ou de feuille ne soit pas dans le bon format. Veuillez redémarrer le programme complètement afin de corriger votre saisie. Le programme doit s-arrêter ici."
	assert "xlsx" in fichier, "ERREUR FATALE : Il semble que vous essayer d-utiliser ce programme avec un fichier qui n-est pas XLSX. Ce programme est incompatible avec des fichiers qui ne sont pas au format XLSX. Veuillez redémarrer complètement le programme afin de corriger votre saisie. Le programme doit s-arrêter ici."
	classeur=load_workbook(fichier)
	feuille=classeur[feuille]

print("\nERREUR FATALE : Cette fonction ne peut pas être utilisée en mode standalone.")
print("Veuillez lancer le programme complet à partir du fichier main.py.")
print("Le programme doit s-arrêter ici.")
quit()