# Sauf mention explicite, les instructions d’un programme s’exécutent les unes après les autres,  dans
# l’ordre où elles ont été écrites à l’intérieur du script.
# Cette  affirmation  peut  vous  paraître  banale  et  évidente  à  première  vue.  L’expérience  montre
# cependant qu’un grand nombre d’erreurs sémantiques dans les programmes d’ordinateur sont la
# conséquence  d’une mauvaise disposition  des  instructions. Plus vous progresserez dans  l’art de la
# programmation, plus vous vous rendrez compte qu’il faut être extrêmement attentif à l’ordre dans
# lequel vous placez vos instructions les unes derrière les autres.
# Par exemple, dans la séquence d ’instructions suivantes :
# >>> a, b = 3, 7
# >>> a = b
# >>> b = a
# >>> print(a, b)
# Vous obtiendrez un résultat contraire si vous intervertissez les 2e et 3e lignes
# <<Exemple 1>>

# Tel qu’il est utilisé ici, le terme de  séquence désigne donc une série d’instructions qui se suivent. Nous
# préférerons dans la suite de cet ouvrage réserver ce terme à un concept Python précis, lequel englobe les
# chaînes de caractères, les tuples et les listes(voir plus loin).

# Python exécute normalement les instructions de la première à la dernière, sauf lorsqu ’il rencontre une
# instruction conditionnelle comme l’instruction if décrite ci-après (nous en rencontrerons d’autres plus
# loin,  notamment  à  propos  des  boucles  de  répétition).  Une  telle  instruction  va  permettre  au
# programme de suivre différents chemins suivant les circonstances

if __name__ == '__main__':
    # <<Exemple 1>>
    # premier cas
    a, b = 3, 7  # 1
    a = b  # 2   a = 7 et b = 7
    b = a  # 3   b = 7 et a = 7
    print("1er cas -> a vaut:", a, "b vaut:", b)  # 4

    # deuxieme cas
    a, b = 3, 7  # 1
    b = a  # 3   b = 3 et a = 3
    a = b  # 2   a = 3 et b = 3
    print("2nd cas -> a vaut:", a, "b vaut:", b)  # 4
