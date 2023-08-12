# Nous  savons  désormais  comment  choisir  judicieusement  un  nom  de  variable.  Voyons  à  présent
# comment nous pouvons définir une variable et lui affecter une valeur. Les termes « affecter une valeur »
# ou « assigner une valeur » à une variable sont équivalents. Ils désignent l’opération par laquelle on
# établit un lien entre le nom de la variable et sa valeur (son contenu).
# En Python comme dans de nombreux autres langages, l’opération d’affectation est représentée par le
# signe égale =
# <<Exemple 1>>

# Les noms commençant par une majuscule ne sont pas interdits, mais l ’usage veut qu’on le réserve plutôt
# aux variables qui désignent des classes(le concept de classe sera abordé plus loin dans cet ouvrage).
#
# Il arrive
# aussi que l’on écrive entièrement en majuscules certaines variables que l’on souhaite traiter comme des
# pseudo-constantes (c’est-à-dire des variables que l’on évite de modifier au cours du programme).

# >>> n = 7  # définir la variable n et lui donner la valeur 7
# >>> msg = "Quoi de neuf ?"  # affecter la valeur "Quoi de neuf ?" à msg
# >>> pi = 3.14159  # assigner sa valeur à la variable pi
# Les exemples ci-dessus illustrent des instructions d’affectation Python tout à fait classiques. Après
# qu’on les ait exécutées, il existe dans la mémoire de l’ordinateur, à des endroits différents :
# • trois noms de variables, à savoir n, msg et pi ;
# • trois séquences d’octets, où sont encodées le nombre entier  7, la chaîne de caractères  Quoi de
# neuf ? et le nombre réel 3,14159.

# Les trois instructions d’affectation ci-dessus ont eu pour effet chacune de réaliser plusieurs opérations
# dans la mémoire de l’ordinateur :
# • créer et mémoriser un nom de variable ;
# • lui attribuer un type bien déterminé (ce point sera explicité à la page suivante) ;
# • créer et mémoriser une valeur particulière ;
# • établir un lien (par un système interne de pointeurs) entre le nom de la variable et l ’emplacement
# mémoire de la valeur correspondante.

# Les trois noms de variables sont des  références, mémorisées dans une zone particulière de la mémoire
# que l’on appelle espace de noms, alors que les valeurs correspondantes sont situées ailleurs, dans des
# emplacements parfois fort éloignés les uns des autres. Nous aurons l’occasion de préciser ce concept
# plus loin dans ces pages

if __name__ == '__main__':
    # <<Exemple 1>>
    n = 7  # définir la variable n et lui donner la valeur 7
    msg = "Quoi de neuf ?"  # affecter la valeur "Quoi de neuf ?" à msg
    pi = 3.14159  # assigner sa valeur à la variable pi

    print(f" n vaut {n} \n msg vaut {msg} \n pi vaut {pi}")
