# petite documentation

# Les dictionnaires dans un langage de programmation sont un type de structure de données utilisé pour stocker des
# informations connectées d'une manière ou d'une autre. Le dictionnaire Python est défini en deux éléments Keys et
# Values. Les dictionnaires ne stockent pas leurs informations dans un ordre particulier, vous ne pouvez donc pas
# récupérer vos informations dans le même ordre que vous les avez saisies. Les clés seront un seul élément Les
# valeurs peuvent être une liste ou une liste dans une liste, des nombres, etc. Plus d'une entrée par clé n'est pas
# autorisée (aucune clé en double n'est autorisée) Les valeurs du dictionnaire peuvent être de n'importe quel type,
# tandis que les clés doivent être immuables comme les nombres, les tuples ou les chaînes. Les clés de dictionnaire
# sont sensibles à la casse - Le même nom de clé mais avec des cas différents est traité comme des clés différentes
# dans les dictionnaires Python.

if __name__ == '__main__':
    # syntaxe du dictionnaire
    _dict = {"Nom": "Noubouossie", "prenom": "Franck"}

    print(f"dict vaut: {_dict}")

    # afficher une propriete du disctionaire
    print(f"le prenom vaut {_dict['prenom']}")

    # copy de dictionnaire
    _dict1 = _dict.copy()

    print(f"disc1 vaut: {_dict1}")

    # mise a jour de dictionaire
    _dict.update({"prenom": "Herve"})

    print(f"disc vaut: {_dict}")

    # suprimer une cle d'un dictionaire
    del _dict1["prenom"]

    print(f"disc1 vaut: {_dict1}")

    # la methode items du disctionnaire
    # cette methode renvoit une liste de tuple a deux elements
    print(_dict.items())

    # verifier si une cle existe dans le disctionaire
    if "prenom" in _dict.keys():
        print("le key prenom est present dans le disctionnaire _dict")
    else:
        print("le key prenom n'est pas present dans le disctionnaire _dict")

    if "prenom" in _dict1.keys():
        print("le key prenom est present dans le disctionnaire _dict1")
    else:
        print("le key prenom n'est pas present dans le disctionnaire _dict1")

    # classer un dictionnaire
    listCles = list(_dict.keys())

    # listCles.sort(reverse=True)

    for cle in listCles:
        print(f"voici une cle: {cle} et sa valeur: {_dict[cle]}")

    # taille d'un dictionnaire
    print(f"le dictionnaire _dict contient {len(_dict)} elements")

    # comparaison entre plusaieurs dictionnaires
    # ici, on utilise la metode cmp() qui retourne 0 si les dic
    # sont egales, 1 si le premier depasse le second et -1 si le
    # second depasse le premier
    # print(f"comparaison entre _dict et _dict1 {cmp(_dict,_dict1)}")
    # Ca ne fonctionne pas car nous utilisons python3


