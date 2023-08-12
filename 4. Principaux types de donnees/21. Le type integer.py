# Les données numériques
# Dans les exercices réalisés jusqu’à présent, nous avons déjà utilisé des données de deux types : les
# nombres entiers ordinaires et les nombres réels (aussi appelés nombres à virgule flottante). Tâchons de
# mettre en évidence les caractéristiques (et les limites) de ces concepts.

# Le type integer
# soit le bloc d'instrution suivant. Avec while  c < 50:,  nous  devrions  obtenir
# quarante-neuf  termes.
# variable principale :
# a, b, c = 1, 1, 1
#
#     while c < 50:
#         print(f"{c} : {b} {type(b)}")
#         a, b, c = b, a + b, c + 1
# ...
# ... (affichage des 43 premiers termes)
# ...
# 44 : 1134903170 <class 'int'>
# 45 : 1836311903 <class 'int'>
# 46 : 2971215073 <class 'int'>
# 47 : 4807526976 <class 'int'>
# 48 : 7778742049 <class 'int'>
# 49 : 12586269025 <class 'int'>
# <<Exemple 1>>

# Que pouvons-nous constater ? Il semble que Python soit capable de traiter des nombres entiers de
# taille illimitée. La fonction type() nous permet de vérifier à chaque itération que le type de la variable
# reste bien en permanence de ce type.

# L’exercice  que  nous  venons  de  réaliser  pourrait  cependant  intriguer  ceux  d’entre  vous  qui
# s’interrogent sur la représentation interne des nombres dans un ordinateur. Vous savez probablement
# en effet que le cœur de celui-ci est constitué par un circuit intégré électronique (une puce de silicium)
# à  très  haut  degré  d’intégration,  qui  peut  effectuer  plus  d’un  milliard  d’opérations  en  une  seule
# seconde, mais seulement sur des nombres binaires de taille limitée  : 32 bits actuellement

# Or, la gamme de valeurs décimales qu’il est possible d’encoder sous forme de nombres binaires de 32 bits
# s’étend de -2 147 483 648 à +2 147 483 647.
# Les opérations effectuées sur des entiers compris entre ces deux limites  sont donc toujours très
# rapides, parce que le processeur est capable de les traiter directement. En revanche, lorsqu’il est
# question de traiter des nombres entiers plus grands, ou encore des nombres réels (nombres «  à virgule
# flottante »), les logiciels que sont les interpréteurs et compilateurs doivent effectuer un gros travail de
# codage/décodage, afin de ne présenter en définitive au processeur que des opérations binaires sur des
# nombres entiers, de 32 bits au maximum.

# Vous n’avez pas à vous préoccuper de ces considérations techniques. Lorsque vous lui demandez de
# traiter des entiers quelconques, Python les transmet au processeur sous la forme de nombres binaires
# de 32 bits chaque fois que c’est possible, afin d’optimiser la vitesse de calcul et d’économiser l’espace
# mémoire.  Lorsque  les  valeurs  à  traiter  sont  des  nombres  entiers  se  situant  au-delà  des  limites
# indiquées plus haut, leur encodage dans la mémoire de l’ordinateur devient plus complexe, et leur
# traitement  par  le  processeur  nécessite  alors  plusieurs  opérations  successives.  Tout  cela  se  fait
# automatiquement, sans que vous n’ayez à vous en soucier
# <<Exemple 2>>

if __name__ == '__main__':
    # <<Exemple 1>>
    # suite de fibonatchi
    # a, b, c = 1, 1, 1
    #
    # while c < 50:
    #     print(f"c-->{c} : b-->{b} type(b)-->{type(b)}")
    #     a, b, c = b, a + b, c + 1

    # <<Exemple 2>>
    a, b, c = 3, 2, 1
    while c < 15:
        print(f"c-->{c} : b-->{b}")
        a, b, c = b, a * b, c + 1
    # Dans l’exemple ci-dessus, la valeur des nombres affichés augmente très rapidement, car chacun d ’eux
    # est égal au produit des deux termes précédents. Bien évidemment, vous pouvez continuer cette suite
    # mathématique si vous voulez. La progression continue avec des nombres gigantesques, mais la vitesse
    # de calcul diminue au fur et à mesure.
    # Les entiers de valeur comprise entre les deux limites indiquées plus haut occupent
    # chacun 32 bits dans la mémoire de l’ordinateur. Les très grands entiers occupent une
    # place variable, en fonction de leur taille
