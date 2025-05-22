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

def charger_colonnes(fichierc,ligne_depart=2,nb_radios,col_phys,col1,col2,col3=None,col4=None,col5=None,col6=None):
	"""
	Cette fonction permet de charger un certain nombre de colonnes d'un tableau situé dans une feuille.
	Les colonnes sont sélectionnées par leur nom.
	Ce programme ne peut pas supporter plus de 6 colonnes au total.
	Entrée : fichierc (tpl), ligne_depart(int), nb_radios(int), col_phys(str), col1(str, colonne de l-adresse MAC radio 1), col2(str), col3(str), col4(str), col5(str), col6(str)
	Sortie : super_tuple(tpl)
	"""
	assert isinstance(fichierc,tpl) and isinstance(ligne_depart,int) and isinstance(nb_radios,int) and isinstance(col_phys,str) and isinstance(col1,str) and isinstance(col2,str) and (isinstance(col3,str) or col3==None) and (isinstance(col4,str) or col4==None) and (isinstance(col5,str) or col5==None) and (isinstance(col6,str) or col6==None), "ERREUR FATALE : Les informations entrées en paramètres de cette fonction ne sont pas dans le bon format. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert nb_radios<=6, "ERREUR FATALE : Cette fonction ne peut prendre en charge un appareil qui a plus de 6 antennes radio. Veuillez redémarrer le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert ligne_depart>0, "ERREUR FATALE : La ligne où se situe vos entêtes de colonnes ne peut pas être inférieure ou égale à zéro. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	# On charge le contenu de la feuille à modifier dans des variables.
	contenu_feuille=fichierc[1]
	# Ensuite, on créé un dictionnaire. Pour chaque nom de colonne, on lui associe un index qui correspond au nom de colonne Excel (A,B,C,D, etc.). Ainsi, Python peut savoir avec précision quelle colonne se situe où dans la feuille.
	dico_colonnes={cellule.value:numero for numero,cellule in enumerate(contenu_feuille[ligne_depart])}
	# Enfin, on remplit les variables avec les bonnes valeurs et on retourne un beau tuple.
	colonne_mac_phys=dico_colonnes[col_phys]
	colonne1=dico_colonnes[col1]
	colonne2=dico_colonnes[col2]
	tableau_final=[colonne_mac_phys,colonne1,colonne2]
	if type(col3)==str:
		colonne3=dico_colonnes[col3]
		tableau_final.append(colonne3)
	elif type(col4)==str:
		colonne4=dico_colonnes[col4]
		tableau_final.append(colonne4)
	elif type(col5)==str:
		colonne5=dico_colonnes[col5]
		tableau_final.append(colonne5)
	elif type(col6)==str:
		colonne6=dico_colonnes[col6]
		tableau_final.append(colonne6)
	super_tuple=tuple(tableau_final)
	return super_tuple

print("\nERREUR FATALE : Cette fonction ne peut pas être utilisée en mode standalone.")
print("Veuillez lancer le programme complet à partir du fichier main.py.")
print("Le programme doit s-arrêter ici.")
quit()