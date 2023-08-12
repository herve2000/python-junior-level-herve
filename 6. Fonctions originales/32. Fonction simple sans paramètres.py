# Pour notre première  approche concrète des fonctions,  nous allons travailler à nouveau en mode
# interactif. Le mode interactif de Python est en effet idéal pour effectuer des petits tests comme ceux
# qui suivent. C’est une facilité que n’offrent pas tous les langages de programmation !
# >>> def table7():
# ... n = 1
# ... while n <11 :
# ... print(n * 7, end =' ')
# ... n = n +1
# ...
# <<Exemple 1>>

# En entrant ces quelques lignes, nous avons défini une fonction très simple qui calcule et affiche les 10
# premiers termes de la table de multiplication par 7. Notez bien les parenthèses, le double point, et
# l’indentation du bloc d’instructions qui suit la ligne d ’en-tête (c’est ce bloc d’instructions qui constitue
# le corps de la fonction proprement dite).
# Pour utiliser la fonction que nous venons de définir, il suffit de l’appeler par son nom. Ainsi :
# >>> table7()
# provoque l’affichage de :
# 7 14 21 28 35 42 49 56 63 70

# Nous pouvons maintenant réutiliser cette fonction à plusieurs reprises, autant de fois que nous le
# souhaitons. Nous pouvons également l’incorporer dans la définition d ’une autre fonction, comme dans
# l’exemple ci-dessous :
# >>> def table7triple():
# ... print('La table par 7 en triple exemplaire :')
# ... table7()
# ... table7()
# ...
# <<Exemple 2>>

# Utilisons cette nouvelle fonction, en entrant la commande :
# >>> table7triple()
# l’affichage résultant devrait être :
# La table par 7 en triple exemplaire :
# 7 14 21 28 35 42 49 56 63 70
# 7 14 21 28 35 42 49 56 63 70
# 7 14 21 28 35 42 49 56 63 70


# Une première fonction peut donc  appeler une deuxième  fonction, qui elle-même en  appelle  une troisième,
# etc. Au stade où nous sommes, vous ne voyez peut-être pas encore très bien l ’utilité de tout cela,
# mais vous pouvez déjà noter deux propriétés intéressantes :
# • Créer une nouvelle fonction vous offre l’opportunite de donner un nom à tout un ensemble d’instructions.
# De  cette  manière,  vous  pouvez  simplifier  le  corps principal  d ’un  programme,  en dissimulant  un
# algorithme  secondaire  complexe  sous  une  commande  unique, à  laquelle vous pouvez donner un nom très explicite,
# en français si vous voulez.
# • Créer une nouvelle fonction peut servir à raccourcir un programme, par élimination des portions de code
# qui se répètent. Par exemple, si vous devez afficher la table par 7 plusieurs fois dans un même programme,
# vous n’avez pas à réécrire chaque fois l’algorithme qui accomplit ce travail. Une fonction est donc en quelque
# sorte une nouvelle instruction personnalisée, que vous ajoutez vous-même librement à votre langage de programmation


def table7():
    n = 1
    while n < 11:
        print(n * 7, end=' ')
        n = n + 1

    print("\n")


def table8():
    n = 1
    while n < 11:
        print(n * 8, end=' ')
        n = n + 1

    print("\n")


def table7triple():
    print('La table par 7 en triple exemplaire : \n')
    table7()
    table7()
    table7()


if __name__ == '__main__':
    # <<Exemple 1>>
    table8()

    # <<Exemple 2>>
    # table7triple()
