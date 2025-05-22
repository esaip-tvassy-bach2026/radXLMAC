"""
Ce fichier contient toutes les fonctions qui permettent la modification et la sauvegarde du fichier Excel.
"""
from copier import copie
from chargement import charger, charger_colonnes
from formater import mise_au_format, additionner_MAC

def remplir_colonnes(fichier_charge,colonnes,nb_radios,ligne_base=2):
	"""
	Cette fonction permet de remplir les cellules du fichier Excel avec les bonnes adresses MAC.
	Entrée : fichier_charge(tpl), colonnes(tpl), nb_radios(int), ligne_base(int)
	Sortie : message_fin(str)
	"""
	assert isinstance(fichier_charge,tuple) and isinstance(colonnes,tuple) and isinstance(nb_radios,int) and isinstance(ligne_base,int), "ERREUR FATALE : Les arguments passés en paramètres de cette fonction sont incorrects ou pas dans les bons formats. Veuillez redémarrer le programme complètement et corriger votre saisie. Le programme doit s-arrêter ici."
	assert nb_radios<=6, "ERREUR FATALE : Cette fonction ne peut pas traiter plus de 6 antennes radios en même temps. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
	assert ligne_base>0, "ERREUR FATALE : La ligne de votre fichier Excel où se situe les colonnes de votre tableau est incorrecte. Elle ne peut pas être égale ou inférieure à zéro. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."