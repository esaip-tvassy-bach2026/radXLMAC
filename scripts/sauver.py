"""
Ce fichier contient toutes les fonctions qui permettent la modification et la sauvegarde du fichier Excel.
"""
from copier import copie
from chargement import charger, charger_colonnes
from formater import mise_au_format, additionner_MAC

def remplir_colonnes(fichier_charge,colonnes,nb_radios,ligne_base=2,formater):
	"""
	Cette fonction permet de remplir les cellules du fichier Excel avec les bonnes adresses MAC.
	Entrée : fichier_charge(tpl), colonnes(tpl), nb_radios(int), ligne_base(int),formater(bool)
	Sortie : message_fin(str)
	"""
	assert isinstance(fichier_charge,tuple) and isinstance(colonnes,tuple) and isinstance(nb_radios,int) and isinstance(ligne_base,int) and isinstance(formater,bool), "ERREUR FATALE : Les arguments passés en paramètres de cette fonction sont incorrects ou pas dans les bons formats. Veuillez redémarrer le programme complètement et corriger votre saisie. Le programme doit s-arrêter ici."
	assert nb_radios<=6, "ERREUR FATALE : Cette fonction ne peut pas traiter plus de 6 antennes radios en même temps. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert ligne_base>0, "ERREUR FATALE : La ligne de votre fichier Excel où se situe les colonnes de votre tableau est incorrecte. Elle ne peut pas être égale ou inférieure à zéro. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	classeur=fichier_charge[0]
	feuille=fichier_charge[1]
	col_mac_physique=colonnes[0]
	col_radio=[]
	for i in range(1, nb_radios+1):
		if i<len(colonnes):
			col_radio.append(colonnes[i])
	# On parcourt toutes les lignes du tableau pour les remplir.
	for rangee in feuille.iter_rows(min_row=ligne_base+1,max_col=feuille.max_column):
		mac_cellule=rangee[col_mac_physique-1]
		mac_valeur=mac_cellule.value
		if mac_valeur:
			# Formatage de l-adresse MAC Physique.
			mac_physique_formatee=mise_au_format(mac_valeur)
			if formater==True:
				mac_cellule.value=mac_physique_formatee
			# Utilisation de l-adresse MAC Physique formatée pour faire les calculs.
			mac_base=mac_physique_formatee.replace(":","")
			# Remplissage des adresses radios.
			for idx_radio,col_idx in enumerate(col_radio):
				mac_radio=additionner_MAC(mac_base,idx_radio+1)
				mac_radio_formatee=mise_au_format(mac_radio)
				if formater==True:
					rangee[col_idx-1].value=mac_radio_formatee
				else:
					rangee[col_idx-1].value=mac_radio