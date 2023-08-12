# Vous avez déjà rencontré précédemment cet autre type de donnée numérique  : le type « nombre
# réel », ou « nombre à virgule flottante », désigné en anglais par l’expression floating  point  number, et
# que pour cette raison on appellera type float sous Python.

# Ce type autorise les calculs sur de très grands ou très petits nombres (données scientifiques, par
# exemple), avec un degré de précision constant.
# Pour qu’une donnée numérique soit considérée par Python comme étant du type  float, il suffit qu’elle
# contienne dans sa formulation un élément tel qu’un point décimal ou un exposant de 10.
# Par exemple, les données :
# 3.14 10. .001 1e100 3.14e-10
# sont automatiquement interprétées par Python comme étant du type float.
# <<Exemple 1>>

# Essayons donc ce type de données dans un nouveau petit programme (inspiré du précédent) :
# >>> a, b, c = 1., 2., 1   # => a et b seront du type 'float'
# >>> while c < 18:
# ... a, b, c = b, b*a, c+1
# ... print(b)
# <<Exemple 2>>

# Comme vous l’aurez certainement bien compris, nous affichons cette fois encore une série dont les
# termes augmentent extrêmement vite, chacun d’eux étant égal au produit des deux précédents. Au
# neuvième terme, Python passe automatiquement à la notation scientifique («  e+n » signifie en fait :
# « fois dix à l’exposant n »). Après le quinzième terme, nous assistons à nouveau à un dépassement de
# capacité  (sans message d’erreur) :  les nombres vraiment trop grands  sont  tout simplement notés
# « inf » (pour « infini »).
# Le  type  float utilisé  dans  notre  exemple  permet  de  manipuler  des  nombres  (positifs  ou  négatifs)
# compris entre 10^-308 et 10^308
# avec une précision de 12 chiffres significatifs. Ces nombres sont encodés
# d’une manière particulière sur 8 octets (64 bits) dans la mémoire de la machine  : une partie du code
# correspond aux 12 chiffres significatifs, et une autre à l’ordre de grandeur (exposant de 10)


if __name__ == '__main__':
    # <<Exemple 1>>
    # print(f"le type de la valeur 3.14 est {type(3.14)}")
    # print(f"le type de la valeur 10. est {type(10.)}")
    # print(f"le type de la valeur .001 est {type(.001)}")
    # print(f"le type de la valeur 1e100 est {type(1e100)}")
    # print(f"le type de la valeur 3.14e-10 est {type(3.14e-10)}")

    # <<Exemple 2>>
    a, b, c = 1., 2., 1  # => a et b seront du type 'float'
    while c < 18:
        print("c-->", c, "b-->", b, "type(b)-->", type(b))
        a, b, c = b, b * a, c + 1
