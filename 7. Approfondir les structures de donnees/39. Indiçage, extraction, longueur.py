# Petit rappel du chapitre 5 : les chaînes sont des séquences de caractères. Chacun de ceux-ci occupe une
# place précise dans la séquence. Sous Python, les éléments d’une séquence sont toujours  indicés (ou
# numérotés) de la même manière, c’est-à-dire à partir de zéro. Pour extraire un caractère d ’une chaîne, il
# suffit d’accoler au nom de la variable qui contient cette chaîne, son indice entre crochets :
# >>> nom = 'Cédric'
# >>> print(nom[1], nom[3], nom[5])
# é r c
# <<Exemple 1>>
#
# Il est souvent utile de pouvoir désigner l’emplacement d’un caractère par rapport à la fin de la chaîne. Pour cela,
# il suffit d’utiliser des indices négatifs. Ainsi -1 désignera le dernier caractère,  -2 l’avant dernier, etc.
# : >>> print (nom[-1], nom[-2], nom[-4], nom[-6]) cid
# <<Exemple 2>>
# >>> Si l’on désire déterminer le nombre de caractères présents dans
# une chaîne, on utilise la fonction intégrée len() :
# >>> print(len(nom)) 6
# <<Exemple 3>>


if __name__ == '__main__':
    # <<Exemple 1>>
    nom = 'Cédric'
    print(nom[1], nom[3], nom[5])

    # <<Exemple 2>>
    print(nom[-1], nom[-2], nom[-4], nom[-6])

    # <<Exemple 3>>
    print(len(nom))
