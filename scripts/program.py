"""
Ce fichier contient le cerveau du programme. C-est le fichier central du programme.
"""
from copier import copie
from chargement import charger, charger_colonnes
from sauver import remplir_colonnes, sauvegarde_finale
from formater import mise_au_format, recuperation_increments, additionner_MAC

def cerveau_principal(former,nom_fichier_init,nom_feuille_init,nom_col_mac_B,nbr_rad,nom_col_mac_RAD,ligne_base=2):
	"""
	Cette fonction est le cerveau du programme.
	Elle permet de lancer toutes les autres fonctions, avec les souhaits de l-utilisateur.
	Entrée : former(bool), nom_fichier_init(str), nom_feuille_init(str), nom_col_mac_B(str), nbr_rad(int), nom_col_mac_RAD(str), ligne_base(int)
	Sortie : message_de_fin(str)
	"""
	assert isinstance(former,bool) and isinstance(nom_fichier_init,str) and isinstance(nom_feuille_init,str) and isinstance(nom_col_mac_B,str) and isinstance(nbr_rad,int) and isinstance(nom_col_mac_RAD,str) and isinstance(ligne_base,int), "ERREUR FATALE : Les informations entrées en paramètres de cette fonction sont incorrectes ou sont dans un mauvais format. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert "xlsx" in nom_fichier_init, "ERREUR FATALE : Il semble que vous essayez d-utiliser un fichier qui n-est pas au format XLSX. Ce programme n-est pas compatible avec le type de fichier que vous essayer d-utiliser. Veuillez redémarrer le programme complètement et corriger votre saisie. Le programme doit s-arrêter ici."
	assert nbr_rad<=6, "ERREUR FATALE : Ce programme ne peut pas calculer les adresses MAC de plus de 6 antennes radios en même temps. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert ligne_base>0, "ERREUR FATALE : Le numéro de la ligne où se situe vos entêtes de colonnes ne peut pas être inférieure ou égale à zéro. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	# En premier, on copie le fichier d-origine.
	copie(nom_fichier_init,"votre_nouvelle_archive_modifiee.xlsx")