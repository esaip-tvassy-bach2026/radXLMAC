"""
Ce fichier contient le cerveau du programme. C-est le fichier central du programme.
"""
from copier import copie
from chargement import charger, charger_colonnes
from sauver import remplir_colonnes, sauvegarde_finale

def cerveau_principal(former,fichier_source,feuille_cible,nom_col_mac_B,nbr_rad,nom_col_mac_RAD,ligne_base=2):
	"""
	Cette fonction est le cerveau du programme.
	Elle permet de lancer toutes les autres fonctions, avec les souhaits de l-utilisateur.
	Entrée : former(bool), fichier_source(str), feuille_cible(str), nom_col_mac_B(str), nbr_rad(int), nom_col_mac_RAD(str), ligne_base(int)
	Sortie : message_de_fin(str)
	"""
	assert isinstance(former,bool) and isinstance(fichier_source,str) and isinstance(feuille_cible,str) and isinstance(nom_col_mac_B,str) and isinstance(nbr_rad,int) and isinstance(nom_col_mac_RAD,str) and isinstance(ligne_base,int), "ERREUR FATALE : Les informations entrées en paramètres de cette fonction sont incorrectes ou sont dans un mauvais format. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert "xlsx" in fichier_source, "ERREUR FATALE : Il semble que vous essayez d-utiliser un fichier qui n-est pas au format XLSX. Ce programme n-est pas compatible avec le type de fichier que vous essayer d-utiliser. Veuillez redémarrer le programme complètement et corriger votre saisie. Le programme doit s-arrêter ici."
	assert nbr_rad<=6, "ERREUR FATALE : Ce programme ne peut pas calculer les adresses MAC de plus de 6 antennes radios en même temps. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert ligne_base>0, "ERREUR FATALE : Le numéro de la ligne où se situe vos entêtes de colonnes ne peut pas être inférieure ou égale à zéro. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	fichier_new="ma_superbe_archive_modifiee.xlsx"
	# Première étape : on fait une copie d'origine.
	copie(fichier_source,fichier_new)
	# Deuxième étape : on charge le fichier et les données nécessaires.
	fichier_charge=charger(fichier_new,feuille_cible)
	# Troisième étape : détection des colonnes à modifier.
	noms_colonnes_radio=[f"{nom_col_mac_RAD} {i+1}" for i in range(nbr_rad)]
	params_colonnes=[fichier_charge,ligne_base,nbr_rad,nom_col_mac_B]+nom_col_mac_RAD
	colonnes=charger_colonnes(*params_colonnes)
	# Quatrième étape : on modifie le fichier aux bons endroits.
	remplir_colonnes(fichier_charge,colonnes,nbr_rad,ligne_base,former)
	# Cinquième étape : on enregistre le fichier modifié.
	sauvegarde_finale(fichier_charge,fichier_new)
	# Message de fin.
	message_de_fin=f"Fini ! Votre archive avec les adresses MAC calculées est {fichier_new}."
	return message_de_fin

print("ERREUR FATALE : Vous ne pouvez pas lancer cette fonction en mode standalone.")
print("Veuillez lancer le programme en exécutant son fichier principal, main.py.")
print("Le programme doit s-arrêter ici.")
quit()