# La fonction  table() est certainement intéressante, mais elle n ’affiche toujours que les dix premiers
# termes de la table de multiplication, alors que nous pourrions souhaiter qu ’elle en affiche d’autres.
# Qu’à cela ne tienne. Nous allons l’améliorer en lui ajoutant des paramètres supplémentaires, dans une
# nouvelle version que nous appellerons cette fois tableMulti() :
# >>> def tableMulti(base, debut, fin):
# ... print('Fragment de la table de multiplication par', base, ':')
# ... n = debut
# ... while n <= fin :
# ... print(n, 'x', base, '=', n * base)
# ... n = n +1

# Cette nouvelle fonction utilise donc trois paramètres : la base de la table comme dans l ’exemple
# précédent, l’indice du premier terme à afficher, l’indice du dernier terme à afficher.
# Essayons cette fonction en entrant par exemple :
# >>> tableMulti(8, 13, 17)
# <<Exemple 1>>

# ce qui devrait provoquer l’affichage de :
# Fragment de la table de multiplication par 8 :
# 13 x 8 = 104
# 14 x 8 = 112
# 15 x 8 = 120
# 16 x 8 = 128
# 17 x 8 = 136

# Notes
# • Pour  définir  une  fonction  avec  plusieurs  paramètres,  il  suffit  d ’inclure  ceux-ci  entre  les
# parenthèses qui suivent le nom de la fonction, en les séparant à l’aide de virgules.
# • Lors de l’appel de la fonction, les arguments utilisés doivent être fournis  dans le même ordre que
# celui des paramètres correspondants (en les séparant eux aussi à l ’aide de virgules). Le premier
# argument  sera  affecté  au  premier  paramètre,  le  second  argument  sera  affecté  au  second
# paramètre, et ainsi de suite.
# • À  titre  d’exercice, essayez  la  séquence d’instructions  suivantes  et  décrivez  dans  votre cahier
# d’exercices le résultat obtenu :
# >>> t, d, f = 11, 5, 10
# >>> while t<21:
# ... tableMulti(t,d,f)
# ... t, d, f = t +1, d +3, f +5
# ...
# <<Exemple 2>>


def tableMulti(base, debut, fin):
    print('Fragment de la table de multiplication par', base, ':', f" debut--> {debut}", f" fin-->{fin}")
    n = debut
    while n <= fin:
        print(n, 'x', base, '=', n * base)
        n = n + 1


if __name__ == '__main__':
    # <<Exemple 1>>
    # tableMulti(8, 13, 17)

    # <<Exemple 2>>
    t, d, f = 11, 5, 10
    while t < 21:
        tableMulti(t, d, f)
        t, d, f = t + 1, d + 3, f + 5
