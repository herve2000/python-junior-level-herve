# Lorsqu’un programme contient des instructions telles que  while ou  if, l’ordinateur qui exécute ce
# programme doit évaluer la véracité d’une condition, c’est-à-dire déterminer si une expression est  vraie
# ou  fausse. Par exemple, une boucle initiée par   while c < 20:  s’exécutera aussi longtemps que la
# condition c < 20 restera vraie.
#
# Mais comment un ordinateur peut-il déterminer si quelque chose est vrai ou faux ?
# En fait – et vous le savez déjà – un ordinateur ne manipule strictement que des nombres. Tout ce qu ’un
# ordinateur doit traiter doit d’abord toujours être converti en valeur numérique. Cela s’applique aussi à
# la notion de vrai/faux. En Python, tout comme en C, en Basic et en de nombreux autres langages de programmation,
# on considère que toute valeur numérique autre que zéro est «  vraie ». Seule la valeur
# zéro est « fausse ».
# Exemple :
# ch = input('Entrez un nombre entier quelconque')
# n = int(ch)
# if n:
# print("vrai")
# else:
# print("faux")
# <<Exemple 1>>

# Le  petit  script  ci-dessus  n’affiche  faux que  si  vous  entrez  la  valeur  0.  Pour  toute  autre  valeur
# numérique, vous obtiendrez vrai.

# Ce qui précède signifie donc qu’une expression à évaluer, telle par exemple la condition  a > 5, est
# d’abord convertie par l’ordinateur en une valeur numérique (1 si l’expression est vraie, et  zéro si
# l’expression est fausse). Ce n’est pas tout à fait évident, parce que l’interpréteur Python est doté d’un
# dispositif qui traduit ces deux valeurs en  True ou  False lorsqu’on les lui demande explicitement.
# Exemple :
# >>> a, b = 3, 8
# >>> c = (a < b)
# >>> d = (a > b)
# >>> c
# True
# >>> d
# False
# <<Exemple 2>>

# En utilisant les valeurs des variables c et d comme indices pour extraire les éléments de la liste  accord,
# nous confirmons bien que False = 0 et True = 1.
# Le petit script ci-après est très similaire au précédent. Il nous permet de tester le caractère vrai ou
# faux d’une chaîne de caractères :
# ch = input("Entrez une chaîne de caractères quelconque")
# if ch:
# print("vrai")
# else:
# print("faux")
# <<Exemple 3>>

# Ces variables sont d’un type entier un peu particulier : le type «  booléen ». Les variables de ce type ne
# peuvent prendre que les deux valeurs True et False (en réalité, 1 et 0).

# Vous obtiendrez  faux pour toute chaîne  vide, et  vrai  pour toute chaîne contenant au moins un
# caractère. Vous pourriez de la même manière tester la «  véracité » d’une liste, et constater qu’une liste
# vide est fausse, alors qu’une liste ayant un contenu quelconque est vraie
#
# L’instruction if ch:, à la troisième ligne de cet exemple, est donc équivalente à une instruction du
# type if ch != "":, du moins de notre point de vue d’êtres humains. Pour l’ordinateur, cependant, ce
# n’est pas tout à fait pareil. Pour lui, l’instruction if ch: consiste à vérifier directement si la valeur de
# la variable  ch est une chaîne vide ou non, comme nous venons de le voir. Cependant, la seconde
# formulation if ch != "": lui impose de commencer par comparer le contenu de  ch  à la valeur d’une
# autre donnée que nous lui fournissons par notre programme(une chaîne vide), puis à évaluer  ensuite si le
# résultat de cette comparaison est lui-même vrai ou  faux (ou en d’autres termes, à vérifier si ce
# résultat est lui-même  True ou  False).
# Cela lui demande donc deux opérations successives, là où la première  formulation  ne  lui  en  demande
# qu’une  seule.  La  première  formulation  est  donc  plus performante.
# Pour les mêmes raisons, dans un script tel celui-ci :
# ch = input("Veuillez entrer un nombre : ")
# n = int(ch)
# if n % 2:
# print("Il s'agit d'un nombre impair.")
# else:
# print("Il s'agit d'un nombre pair.")

# il est plus efficace de programmer la troisième ligne comme nous l’avons fait ci-dessus, plutôt que
# d’écrire  explicitement if n % 2 != 0,  car  cette  formulation  imposerait  à  l’ordinateur  d’effectuer
# deux comparaisons successives au lieu d’une seule.
# Ce raisonnement « proche de la machine » vous paraîtra probablement un peu subtil au début, mais
# croyez bien que cette forme d’écriture vous deviendra très vite tout à fait familière.

if __name__ == '__main__':
    # <<Exemple 1>>
    # ch = input('Entrez un nombre entier quelconque: ')
    # n = int(ch)
    #
    # if n:
    #     print("vrai")
    # else:
    #     print("faux")

    # <<Exemple 2>>
    # a, b = 3, 8
    # c = a < b
    # d = a > b
    #
    # print("c vaut ", c, " et d vaut ", d)
    #
    # # L’expression a < b est évaluée, et son résultat (vrai) est mémorisé dans la variable c. De même pour
    # # le résultat de l’expression inverse, dans la variable d
    # #
    # # À l’aide d’une petite astuce, nous pouvons tout de même vérifier que ces valeurs  True et  False sont
    # # en réalité les deux nombres 1 et 0 « déguisés » :
    # accord = ["non", "oui"]
    #
    # print("Normalement on accede a la premiere valeur en faisant accord[0] qui est ", accord[0])
    # print("Mais on peut aussi y acceder en faisant accord[d] qui est ", accord[d])
    #
    # print("De meme \n")
    #
    # print("Normalement on accede a la seconde valeur en faisant accord[1] qui est ", accord[1])
    # print("Mais on peut aussi y acceder en faisant accord[c] aui est ", accord[c])
    #
    # print("\n ce qui confirme donc les valeurs de c et d")

    # <<Exemple 3>>
    # ch = input("Entrez une chaîne de caractères quelconque: ")
    # if ch:
    #     print("vrai")
    # else:
    #     print("faux")

    liste = ["vrai"]

    if liste:
        print("vrai")
    else:
        print("faux")


