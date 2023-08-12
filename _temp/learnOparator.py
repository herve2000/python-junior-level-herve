# petite documentation

# Les opérateurs d'un langage de programmation sont utilisés pour effectuer diverses opérations sur des valeurs et
# des variables. En Python, vous pouvez utiliser des opérateurs comme
#
# Il existe différentes méthodes de calcul arithmétique en Python car vous pouvez utiliser la fonction eval,
# déclarer une variable et calculer, ou appeler des fonctions Les opérateurs de comparaison souvent appelés
# opérateurs relationnels sont utilisés pour comparer les valeurs de chaque côté d'eux et déterminer la relation
# entre eux Les opérateurs d'affectation Python consistent simplement à affecter la valeur à la variable Python vous
# permet également d'utiliser un opérateur d'affectation composé, dans un calcul arithmétique compliqué,
# où vous pouvez affecter le résultat d'un opérande à l'autre Pour l'opérateur AND - Il renvoie TRUE si les deux
# opérandes (côté droit et côté gauche) sont vrais Pour l'opérateur OR - Il renvoie TRUE si l'un des opérandes (côté
# droit ou côté gauche) est vrai Pour l'opérateur NOT - renvoie TRUE si l'opérande est faux Deux opérateurs
# d'appartenance sont utilisés en Python. (dans, pas dans). Il donne le résultat en fonction de la variable présente
# dans la séquence ou la chaîne spécifiée Les deux opérateurs d'identification utilisés en Python sont (est,
# n'est pas) Elle renvoie true si deux variables pointent vers le même objet et false sinon L'opérateur de priorité
# peut être utile lorsque vous devez définir la priorité pour laquelle le calcul doit être effectué en premier dans
# un calcul complexe.

if __name__ == '__main__':
    # operateur arithmetique
    # adition, soustraction, multiplication, division, modulo,  exponentiel, etc

    a = 5
    b = 6

    # aditions
    print(f"adition a+b= {a + b}")

    # soustraction
    print(f"soustraction a-b= {a - b}")

    # multiplication
    print(f"soustraction a*b= {a * b}")

    # division
    print(f"division a/b= {a / b}")

    # modulo
    print(f"modulo a%b= {a % b}")

    # exponentiel
    print(f"exponentiel a**b= {a ** b}")

    # operateur de comparaison
    # egalite ==, difference != <>, superieur >, inferieur <,
    # inferieur ou egale <=, superieur ou egale >=

    # operateur d'affectation
    # affectation simple =
    # incrementer +=
    # decrementer -=
    # multiplier *=
    # deviser /=

    # operateur logique
    # and, or, not
    print(1 == 2 or (not 2 == 3))

    # memberShip operator
    # in et not in
    _list = [1, 2, 3, 4, 5]
    print(6 not in _list)

    # identify operator
    # cet operateur est utilise en python pour comparer l'emplacement
    # memoire de deux objets. Ce sont is et is not.
    # is retourne vrai si deux variable point le meme objet
