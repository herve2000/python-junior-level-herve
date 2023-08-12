# Les chaînes peuvent être concaténées avec l’opérateur + et répétées avec l’opérateur * :
# >>> n = 'abc'+ 'def'  # concaténation
# >>> m = 'zut ! '* 4  # répétition
# >>> print(n, m)
# <<Exemple 1>>
# abcdef zut ! zut ! zut ! zut !

# Remarquez  au  passage que  les opérateurs  + et  * peuvent  aussi être utilisés pour l ’addition et la
# multiplication lorsqu’ils s’appliquent à des arguments numériques.
#
# Le fait que les mêmes opérateurs puissent  fonctionner  différemment  en  fonction  du  contexte  dans  lequel
# on  les  utilise  est  un mécanisme  fort  intéressant  que  l’on  appelle  surcharge  des  opérateurs.
# Dans  d’autres  langages,  la surcharge des opérateurs n’est pas  toujours possible : on doit alors utiliser des
# symboles différents pour l’addition et la concaténation, par exemple.
# Exercices
# 10.1 Déterminez vous-même ce qui se passe, dans la technique de  slicing, lorsque l’un ou l’autre des
# indices de découpage est erroné, et décrivez cela le mieux possible. (Si le second indice est plus
# petit que le premier, par exemple, ou bien si le second indice est plus grand que la taille de la
# chaîne).
# 10.2 Découpez une grande chaîne en fragments de 5 caractères chacun. Rassemblez ces morceaux
# dans l’ordre inverse.La chaîne doit pouvoir contenir des caractères accentués.
# 10.3 Tâchez d’écrire une petite fonction  trouve() qui fera exactement le contraire de ce que fait
# l’opérateur d’indexage (c’est-à-dire les crochets [  ]). Au lieu de partir d’un index donné pour
# retrouver le caractère correspondant, cette fonction devra retrouver l ’index correspondant à
# un caractère donné.
# En d’autres termes, il s’agit d’écrire une fonction qui attend deux arguments : le nom de la
# chaîne à traiter et le caractère à trouver. La fonction doit fournir en retour l’index du premier
# caractère de ce type dans la chaîne. Ainsi par exemple, l’instruction :
# print(trouve("Juliette & Roméo", "&"))
# devra afficher : 9
# Attention : il faut penser à tous les cas possibles. Il faut notamment veiller à ce que la fonction
# renvoie une valeur particulière (par exemple la valeur -1) si le caractère recherché n ’existe pas
# dans la chaîne traitée. Les caractères accentués doivent être acceptés.
# 10.4 Améliorez la fonction de l’exercice précédent en lui ajoutant un troisième paramètre : l’index à
# partir duquel la recherche doit s’effectuer dans la chaîne. Ainsi par exemple, l’instruction :
# print(trouve ("César & Cléopâtre", "r", 5))
# devra afficher : 15(et non 4 !).
# 10.5 Écrivez une fonction compteCar() qui compte le nombre d’occurrences d’un caractère donné
# dans une chaîne. Ainsi :
# print(compteCar("ananas au jus","a"))
# devra afficher : 4
# print(compteCar("Gédéon est déjà là","é"))
# devra afficher : 3

# -*-coding: utf8 -*-

if __name__ == '__main__':
    # <<Exemple 1>>
    n = 'abc' + 'def'  # concaténation
    m = 'zut ! ' * 4  # répétition
    print(n, m)