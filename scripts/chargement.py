"""
Ce fichier contient le code permettant de charger des fichiers XLSX.
"""
from openpyxl import load_workbook

def charger(fichier,feuille):
	"""
	Cette fonction permet de charger une feuille particulière dans un fichier XLSX.
	Entrée : fichier(str), feuille(str)
	Sortie : tuple_final(tpl)
	"""
	assert isinstance(fichier,str) and isinstance(feuille,str), "ERREUR FATALE : Il semble que votre nom de fichier ou de feuille ne soit pas dans le bon format. Veuillez redémarrer le programme complètement afin de corriger votre saisie. Le programme doit s-arrêter ici."
	assert "xlsx" in fichier, "ERREUR FATALE : Il semble que vous essayer d-utiliser ce programme avec un fichier qui n-est pas XLSX. Ce programme est incompatible avec des fichiers qui ne sont pas au format XLSX. Veuillez redémarrer complètement le programme afin de corriger votre saisie. Le programme doit s-arrêter ici."
	classeur=load_workbook(fichier)
	feuille=classeur[feuille]
	tuple_final=(classeur,feuille)
	return tuple_final

def charger_colonnes(nb_col,col1,col2,col3=None,col4=None,col5=None,col6=None):
	"""
	Cette fonction permet de charger un certain nombre de colonnes d'un tableau situé dans une feuille.
	Les colonnes sont sélectionnées par leur nom.
	Ce programme ne peut pas supporter plus de 6 colonnes au total.
	Entrée : nb_col(int), col1(str, colonne des adresses MAC physiques), col2(str, colonne des adresses MAC radio), col3(str,colonne supplémentaire), col4(str, colonne supplémentaire), col5(str, colonne supplémentaire), col6(str, colonne supplémentaire)
	Sortie : contenu_col1(contenu de la colonne 1), contenu_col2(contenu de la colonne 2), contenu_col3(contenu de la colonne 3), contenu_col4(contenu de la colonne 4), contenu_col5(contenu de la colonne 5), contenu_col6(contenu de la colonne 6)
	"""
	assert isinstance(nb_col,int) and isinstance(col1,str) and isinstance(col2,str) and isinstance(col3,str) and isinstance(col4,str) and isinstance(col5,str) and isinstance(col6,str), "ERREUR FATALE : Il semble que les informations entrées en paramètre de cette fonction soient incorrectes. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert nb_col<=6, "ERREUR FATALE : Cette fonction n-est pas conçue pour supporter plus de 6 colonnes en même temps. Veuillez redémarrer le programme complètement et corriger votre saisie. Le programme doit s-arrêter ici."

print("\nERREUR FATALE : Cette fonction ne peut pas être utilisée en mode standalone.")
print("Veuillez lancer le programme complet à partir du fichier main.py.")
print("Le programme doit s-arrêter ici.")
quit()