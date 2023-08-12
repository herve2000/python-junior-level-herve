# Il arrive très souvent que l’on doive traiter l’intégralité d’une chaîne caractère par caractère, du
# premier jusqu’au dernier, pour effectuer à partir de chacun d ’eux une opération quelconque. Nous
# appellerons cette opération un parcours. En nous limitant aux outils Python que nous connaissons déjà,
# nous pouvons envisager d’encoder un tel parcours à l’aide d’une boucle, articulée autour de l’instruction while :
# >>> nom ="Joséphine"
# >>> index =0
# >>> while index < len(nom):
# ... print(nom[iindex] + ' *', end =' ')
# ... index = index +1
# ...
# J * o * s * é * p * h * i * n * e *
# <<Exemple 1>>

# Cette boucle parcourt donc la chaîne nom pour en extraire un à un tous les caractères, lesquels sont
# ensuite imprimés avec interposition d’astérisques. Notez bien que la condition utilisée avec l’instruction while
# est  index < len(nom), ce qui signifie que le bouclage doit s’effectuer jusqu’à ce que l’on
# soit arrivé à l’indice numéro 9 (la chaîne compte en effet 10 caractères). Nous aurons effectivement
# traité tous les caractères de la chaîne, puisque ceux-ci sont indicés de 0 à 9.
# Le parcours d’une séquence est une opération très fréquente en programmation. Pour en faciliter l ’écriture,
# Python vous propose une structure de boucle plus appropriée que la boucle  while, basée sur le
# couple d’instructions for ... in ... :
# Avec ces instructions, le programme ci-dessus devient  :
# >>> nom ="Cléopâtre"
# >>> for car in nom:
# ... print(car + ' *', end =' ')
# ...
# C * l * é * o * p * â * t * r * e *
# <<Exemple 2>>

# Comme vous pouvez le constater, cette structure de boucle est plus compacte. Elle vous évite d ’avoir à
# définir et à incrémenter une variable spécifique (un «  compteur  ») pour gérer l’indice du caractère que
# vous voulez traiter à chaque itération (c ’est Python qui s’en charge). La structure  for ... in ... ne
# montre que l’essentiel, à savoir que la variable car contiendra successivement tous les caractères de la
# chaîne, du premier jusqu’au dernier.
# L’instruction for permet donc d’écrire des boucles, dans lesquelles l’itération traite successivement tous
# les éléments d’une séquence donnée. Dans l’exemple ci-dessus, la séquence était une chaîne de caractères.
# L’exemple ci-après démontre que l’on peut appliquer le même traitement aux  listes(et il en sera de
# même pour les tuples étudiés plus loin)  :
# liste = ['chien', 'chat', 'crocodile', 'éléphant']
# for animal in liste:
# print('longueur de la chaîne', animal, '=', len(animal))
# L’exécution de ce script donne  :
# longueur de la chaîne chien = 5
# longueur de la chaîne chat = 4
# longueur de la chaîne crocodile = 9
# longueur de la chaîne éléphant = 8
# <<Exemple 3>>

# L’instruction for ... in ... : est un nouvel exemple d’instruction composée. N’oubliez donc pas le double
# point obligatoire à la fin de la ligne, et l’indentation pour le bloc d’instructions qui suit.
# Le nom qui suit le mot réservé in est celui de la séquence qu’il faut traiter. Le nom qui suit le mot réservé
# for est celui que vous choisissez pour la  variable destinée à contenir successivement tous les éléments
# de la séquence. Cette variable est définie automatiquement (c ’est-à-dire qu’il est inutile de la définir au
# préalable), et son type est automatiquement adaptéà celui de l’élément de la séquence qui est en cours de
# traitement  (rappelons  en  effet  que  dans  le  cas  d ’une  liste,  tous  les  éléments  ne  sont  pas
# nécessairement du même type). Exemple  :
# divers = ['lézard', 3, 17.25, [5, 'Jean']]
# for e in divers:
# print(e, type(e))
# L’exécution de ce script donne  :
# lézard <class 'str'>
# 3 <class 'int'>
# 17.25 <class 'float'>
# [5, 'Jean'] <class 'list'>
# <<Exemple 4>>

# Bien que les éléments de la liste divers  soient tous de types différents (une chaîne de caractères, un
# entier, un réel, une liste), on peut affecter successivement leurs contenus à la variable  e, sans que des
# erreurs s’ensuivent (ceci est rendu possible grâce au typage dynamiquedes variables Python).


# Exercices
# 10.6 Dans un conte américain, huit petits canetons s’appellent respectivement :  Jack, Kack, Lack,
# Mack, Nack, Oack, Pack et Qack. Écrivez un petit script qui génère tous ces noms à partir des deux
# chaînes suivantes  :
# prefixes = 'JKLMNOP'et suffixe = 'ack'
# Si vous utilisez une instruction for ... in ..., votre script ne devrait comporter que deux lignes.
# 10.7 Dans un script, écrivez une fonction qui recherche le nombre de mots contenus dans une
# phrase donnée.
# 10.8 Écrivez un script qui recherche le nombre de caractères  e,  é,  è,  ê,  ë contenus dans une phrase
# donnée.


if __name__ == '__main__':
    # <<Exemple 1>>
    # nom = "Joséphine"
    # index = 0
    # while index < len(nom):
    #     print(nom[index] + ' *', end=' ')
    #     index = index + 1

    # <<Exemple 2>>
    # nom = "Cléopâtre"
    # for car in nom:
    #     print(car + ' *', end=' ')

    # <<Exemple 3>>
    # liste = ['chien', 'chat', 'crocodile', 'éléphant']
    # for animal in liste:
    #     print('longueur de la chaîne', animal, '=', len(animal))

    # <<Exemple 4>>
    # divers = ['lézard', 3, 17.25, [5, 'Jean']]
    # for e in divers:
    #     print(e, type(e))

    range()
