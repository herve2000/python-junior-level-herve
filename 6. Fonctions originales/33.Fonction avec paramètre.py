# Dans nos derniers exemples, nous avons défini et utilisé une fonction qui affiche les termes de la table
# de multiplication par 7. Supposons à présent que nous voulions faire de même avec la table par 9. Nous
# pouvons  bien  entendu  réécrire  entièrement  une  nouvelle  fonction  pour  cela.  Mais  si  nous  nous
# intéressons plus tard à la table par 13, il nous faudra encore recommencer.
#
# Ne serait-il donc pas plus intéressant de définir une fonction qui soit capable d’afficher n’importe quelle table,
# à la demande ?
# Lorsque nous appellerons cette fonction, nous devrons bien évidemment pouvoir lui indiquer quelle
# table nous souhaitons afficher. Cette information que  nous  voulons transmettre à la fonction au
# moment même où nous l’appelons s’appelle un  argument.
#
# Nous avons déjà rencontré à  plusieurs reprises des fonctions intégrées qui utilisent des arguments.
# La fonction  sin(a), par exemple, calcule le sinus de l’angle  a. La fonction  sin() utilise donc la valeur
# numérique de  a comme argument pour effectuer son travail.

# Dans la définition d’une telle fonction, il faut prévoir une variable particulière pour recevoir l ’argument transmis.
# Cette variable particulière s’appelle un paramètre. On lui choisit un nom en respectant
# les mêmes règles de syntaxe que d’habitude (pas de lettres accentuées, etc.), et on place ce nom entre
# les parenthèses qui accompagnent la définition de la fonction.
# Voici ce que cela donne dans le cas qui nous intéresse :
# >>> def table(base):
# ... n = 1
# ... while n <11 :
# ... print(n * base, end =' ')
# ... n = n +1
# <<Exemple1>>

# La fonction table() telle que définie ci-dessus utilise le paramètre  base pour calculer les dix premiers
# termes de la table de multiplication correspondante.
# Pour tester cette nouvelle fonction, il nous suffit de l’appeler avec un argument. Exemples :
# >>> table(13)
# 13 26 39 52 65 78 91 104 117 130
# >>> table(9)
# 9 18 27 36 45 54 63 72 81 90

# Dans ces exemples, la valeur que nous indiquons entre parenthèses lors de l’appel de la fonction (et
# qui est donc un argument) est automatiquement affectée au paramètre  base. Dans le corps de la
# fonction,  base joue  le  même  rôle  que  n’importe  quelle  autre  variable.  Lorsque  nous  entrons  la
# commande table(9), nous signifions à la machine que nous voulons exécuter la fonction  table() en
# affectant la valeur 9 à la variable base.


def table(base):
    print("Table de multiplication par ", base)
    n = 1
    while n < 11:
        print(n * base, end=' ')
        n = n + 1
    print("\n")


if __name__ == '__main__':
    # <<Exemple1>>
    table(13)
    table(9)
    table(900)
    table(-5)
    table(1000000)
    table(0)
    table("Ferdinand")


    table(1)
    table(2)
    table(3)

    table(19)
    table(190)
