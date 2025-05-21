"""
Ce fichier contient les fonctions de formatage.
"""

def mise_au_format(adresse):
    """
    Cette fonction met une adresse MAC au format standard, à savoir tout en majuscules et avec des deux-points (:) de séparation.
    Entrée : adresse(str)
    Sortie : Retourne l'adresse MAC dans le bon format.
    """
    assert isinstance(adresse,str), "ERREUR FATALE : L-adresse MAC renseignée n-est pas dans le bon format. Relancez complètement le programme et corrigez votre saisie. Le programme doit s-arrêter ici."
    # Suppression des caractères déjà présents, le cas échéant.
    # On enregistre ça dans une variable.
    adresse_standard=adresse.replace(":","").replace("-","").replace(".","").replace("_","")
    # Vérification du nombre de caractères à nu pour les erreurs de saisie.
    if len(adresse_standard)!=12:
        print("\nERREUR FATALE : Une des adresses MAC de votre tableau, dans votre fichier Excel, n-est pas de 12 caractères. Corrigez votre saisie et redémarrez le programme. Le programme doit s-arrêter ici.")
        quit()
    # On met l'adresse MAC en majuscules.
    adresse_majuscules=adresse_standard.upper()
    print(f"Log : Voici l-adresse MAC en majuscules : {adresse_majuscules}.")
    # On met les deux-points entre les caractères.
    adresse_au_format=":".join([adresse_majuscules[i:i+2] for i in range(0,12,2)])
    print(f"Log : Voici l-adresse MAC finale formatée : {adresse_au_format}.")
    return adresse_au_format

def additionner_MAC(adresse_MAC,nbr_addition):
    """
    Cette fonction permet de faire une additon sur une adresse MAC.
    Par exemple : mon_adresse_MAC+55.
    Entrée : adresse_MAC(str), nbr_addition(int)
    Sortie : adr_additionnee(str)
    """
    assert isinstance(adresse_MAC,str) and isinstance(nbr_addition,int), "ERREUR FATALE : Les informations entrées en paramètres de cette fonction sont incorrectes. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
    calcul=int(adresse_MAC,16)+nbr_addition
    adr_additionnee={:012X}.format(calcul)
    return adr_additionnee