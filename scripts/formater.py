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

def recuperation_increments(nombre_de_radios):
    """
    Cette fonction centrale permet de définir les incrémentations nécessaires pour faire marcher les autres fonctions.
    Entrée : nombre_de_radios(int)
    Sortie : liste_incrementations(lst)
    """
    assert isinstance(nombre_de_radios,int), "ERREUR FATALE : L-argument passé en paramètre de cette fonction est incorrect ou n-est pas dans le bon format. Veuillez redémarrer le programme complètement et corriger votre saisie. Le programme doit s-arrêter ici."
    assert nombre_de_radios<=6, "ERREUR FATALE : Ce programme ne peut pas supporter plus de 6 adresses MAC radio en même temps. Veuillez redémarrer le programme complètement et corriger votre saisie. Le programme doit s-arrêter ici."
    incrementations_possibles=[0x10,0x14,0x20,0x24,0x30,0x34]
    liste_incrementations=[]
    for i in range(nombre_de_radios):
        if i<len(incrementations_possibles):
            liste_incrementations.append(incrementations_possibles[i])
    return liste_incrementations

def additionner_MAC(adresse_MAC,nbr_addition):
    """
    Cette fonction permet de faire une additon sur une adresse MAC.
    Par exemple : mon_adresse_MAC+55.
    Entrée : adresse_MAC(str), nbr_addition(int)
    Sortie : adr_additionnee(str)
    """
    assert isinstance(adresse_MAC,str) and isinstance(nbr_addition,int), "ERREUR FATALE : Les informations entrées en paramètres de cette fonction sont incorrectes. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
    assert nbr_addition>0, "ERREUR FATALE : Votre addition ne peut pas être inférieure ou égale à zéro. Veuillez redémarrer complètement le programme et corriger votre saisie. Le programme doit s-arrêter ici."
    assert nbr_addition
    calcul=int(adresse_MAC,16)+nbr_addition
    adr_additionnee=f"{calcul:012X}"
    return adr_additionnee

print("\nERREUR FATALE : Vous ne pouvez pas exécuter cette fonction en mode standalone.")
print("Veuillez lancer le programme complet en exécutant le fichier main.py.")
print("Le programme doit s-arrêter ici.")
quit()