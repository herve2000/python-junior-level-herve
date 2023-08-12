# Petite documentation
# Fonctions intégrées avec Tuple Pour effectuer différentes tâches, tuple vous permet d'utiliser
# de nombreuses fonctions intégrées telles que all(), any(), enumerate(), max(), min(), sorted(), len(), tuple(), etc.
#
# Avantages du tuple sur la liste L'itération dans le tuple est plus rapide qu'avec la liste, car les tuples sont
# immuables. Les tuples constitués d'éléments immuables peuvent être utilisés comme clé pour le dictionnaire,
# ce qui n'est pas possible avec la liste Si vous avez des données immuables, leur implémentation en tant que tuple
# garantira qu'elles restent protégées en écriture Sommaire Python a une fonctionnalité d'affectation de tuple qui
# vous permet d'affecter plus d'une variable à la fois.
#
# Emballage et déballage de tuples Lors de l'emballage, nous plaçons la valeur dans un nouveau tuple tandis que lors
# de la décompression, nous extrayons ces valeurs dans des variables. Un opérateur de comparaison en Python peut
# fonctionner avec des tuples. Utilisation de tuples comme clés dans les dictionnaires Les tuples sont hachables et
# les listes ne le sont pas Nous devons utiliser tuple comme clé si nous devons créer une clé composite à utiliser
# dans un dictionnaire Le dictionnaire peut renvoyer la liste des tuples en appelant des éléments, où chaque tuple
# est une paire clé-valeur Les tuples sont immuables et ne peuvent pas être supprimés. Vous ne pouvez pas supprimer
# ou supprimer des éléments d'un tuple. Mais supprimer entièrement tuple est possible en utilisant le mot-clé "del"
# Pour récupérer des ensembles spécifiques de sous-éléments à partir d'un tuple ou d'une liste, nous utilisons cette
# fonction unique appelée slicing


if __name__ == '__main__':

    # tuple vide
    # tup1 = ()
    # print(f"tuple vide: tup1 {tup1}")

    # tuple a un element
    # tup1 = (50,)
    # print(f"tuple a un element: tup1 {tup1}")

    # emballage des tuples
    tup1 = ("Noubouossie", "Tchoupe", 2000, "Eleve")

    tup2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    # consulter une valeur specifique
    print(f"la valeur d'index 2 du tuple tup1 est: {tup1[2]}")

    # consuter les valeur comprise entre un index bas(compris) et un
    # autre index haut (non compris dans la selection):
    # notons que le depassement d'index ne declenche pas d'erreur
    print(tup2[0:3])

    # affectation de tuple
    (prenom, nom, dateNaissance, proffession) = tup1

    # # apres l'affectation, nous pouvons acceder aux variables
    # print(f"prenom {prenom}")
    # print(f"nom {nom}")
    # print(f"dateNaissance {dateNaissance}")
    # print(f"proffession {proffession}")
    #
    # # comparrer des tuples
    # # on note ici que la comparaison de tuple entraine la
    # # comparaison des elements de chaque index. si l'un est plus
    # # grand que l'autre, alors on conclut que le premier tuple
    # # est plus grand que le second, si ils ont la meme valeur,
    # # on passe a l'element suivant
    #
    # a = (5, 5)
    # b = (5, 5)
    #
    # if a > b:
    #     print("a est plus grand")
    # elif b > a:
    #     print("b est plus grand")
    # else:
    #     print("a est egale à b")
    #
    # # Utilisation des tuple comme cle dans des dictionnaire
    # a = {"x": 100, "y": 200}
    # b = list(a.items())
    #
    # print(b)
    #
    # # deleting tuple
    # # on ne peut pas suprimer un element specifique d'un tuple,
    # # en revenche, au peut suprimer le tuple lui meme
    # # ici, on utilise le mot cle del
    #
    # a = ("bonjour", "a tous")
    #
    # del a
    #
    # # print(a) declenche une erreur
    #
    # # Decoupage de tuple
    # # le decoupage permet d'obtenir des ensembles specifique
    # # de sous element a partir d'un tuple, d'une liste ou d'un
    # # tableau
    # x = ("a", "b", "c", "d", "e")
    #
    # print(x[2:4])
