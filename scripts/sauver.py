"""
Ce fichier contient toutes les fonctions qui permettent la modification et la sauvegarde du fichier Excel.
"""
from copier import copie
from chargement import charger, charger_colonnes
from formater import mise_au_format, additionner_MAC, recuperation_increments

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
	les_increments=recuperation_increments(nb_radios)
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
				if idx_radio<len(les_increments):
					mac_radio=additionner_MAC(mac_base,les_increments[idx_radio])
					mac_radio_formatee=mise_au_format(mac_radio)
					if formater==True:
						rangee[col_idx-1].value=mac_radio_formatee
					else:
						rangee[col_idx-1].value=mac_radio

def sauvegarde_finale(classeur_modifie,nom_fichier):
	"""
	Cette fonction permet d-enregistrer le fichier modifié une fois que toutes les opérations ont étés réalisées dessus.
	Entrée : classeur_modifie(tpl), nom_fichier(str)
	Sortie : message_reussite(str)
	"""
	assert isinstance(classeur_modifie,tuple) and isinstance(nom_fichier,str), "ERREUR FATALE : Les informations entrées en paramètres de cette fonction sont incorrects ou ne sont pas dans le bon format. Veuillez redémarrer compètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert "xlsx" in nom_fichier, "ERREUR FATALE : Votre nom de fichier de destination ne contient pas l-extension de fichier .xlsx, ce qui est obligatoire. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	classeur_modifie.save(nom_fichier)
	message_reussite="LOG: MSG: Fonction sauvegarde_finale: Le fichier final a bien été sauvegardé dans son nouvel emplacement."
	return message_reussite

print("ERREUR FATALE : Vous ne pouvez pas exécuter cette fonction en mode standalone.")
print("Veuillez lancer le programme principal en exécutant le fichier main.py.")
print("Le programme doit s-arrêter ici.")
quit()