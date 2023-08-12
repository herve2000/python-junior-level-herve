# Il arrive fréquemment, lorsque l’on travaille avec des chaînes, que l ’on souhaite extraire une petite chaîne d’une
# chaîne plus longue. Python propose pour cela une technique simple que l ’on appelle slicing(« découpage en tranches
# »).
#
# Elle consiste à indiquer entre crochets les indices correspondant au début et à la fin de la « tranche » que
# l’on souhaite extraire :
# >>> ch = "Juliette"
# <<Exemple1>>
# >>> print(ch[0:3]) Jul Dans  la  tranche  [n,m],  le  n ième caractère est  inclus,  mais  pas  le  m ième.

# par défaut  : un premier indice non défini est considéré comme zéro, tandis que le second indice omis prend par
# défaut la taille de la chaîne complète :
# >>> print(ch[:3])  # les 3 premiers caractères Jul
# >>> print(ch[3:])  # tout ce qui suit les 3 premiers caractères iette Les caractères accentués ne doivent pas
# faire problème :
# >>> ch = 'Adélaïde'
# >>> print(ch[:3], ch[4:8]) Adé aïde
# <<Exemple 2>>

if __name__ == '__main__':
    # << Exemple1 >>
    ch = "Juliette"
    print(ch[0:3])

    # <<Exemple 2>>
    ch = 'Adélaïde'
    print(ch[:3], ch[4:8])
