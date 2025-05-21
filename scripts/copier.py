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
	assert isinstance(fichier,str) and isinstance(nom_destination,str), "ERREUR FATALE :"