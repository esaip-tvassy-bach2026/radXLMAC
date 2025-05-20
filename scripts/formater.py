"""
Ce fichier contient la fonction de formatage.
"""

def mise_au_format(MAC):
    """
    Cette fonction met une adresse MAC au format standard, à savoir tout en majuscules et avec des deux-points (:) de séparation.
    Entrée : MAC(str)
    Sortie : Retourne l'adresse MAC dans le bon format.
    """
    assert isinstance(MAC,str), "ERREUR FATALE : L-adresse MAC renseignée n-est pas dans le bon format. Relancez complètement le programme et corrigez votre saisie. Le programme doit s-arrêter ici."
    # Suppression des caractères déjà présents, le cas échéant.
    # On enregistre ça dans une variable.
    adresse_standard=MAC.replace(":","").replace("-","").replace(".","").replace("_","")
    # Vérification du nombre de caractères à nu pour les erreurs de saisie.
    if len(adresse_standard)!=12:
        print("\nERREUR FATALE : Une des adresses MAC de votre tableau, dans votre fichier Excel, n-est pas de 12 caractères. Corrigez votre saisie et redémarrez le programme. Le programme doit s-arrêter ici.")
        quit()