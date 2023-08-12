# Si nous voulons  pouvoir écrire  des  applications véritablement utiles, il nous faut des techniques
# permettant d’aiguiller le déroulement du programme dans différentes directions, en fonction des
# circonstances rencontrées. Pour ce faire, nous devons disposer d ’instructions capables de  tester  une
# certaine condition et de modifier le comportement du programme en conséquence.
# La  plus  simple  de  ces  instructions  conditionnelles  est  l’instruction  if.  Pour  expérimenter  son
# fonctionnement, veuillez entrer dans votre éditeur Python les deux lignes suivantes  :
# a = 150
# if a > 100:
#     print("a dépasse la centaine")
# <<Exemple 1>>

# Recommencez le même exercice, mais avec a = 20 en guise de première ligne : cette fois Python n’affiche plus rien.
# L’expression que vous avez placée entre parenthèses après  if est ce que nous appellerons désormais
# une condition.
# L’instruction if permet de tester la validité de cette condition. Si la condition est vraie,
# alors l’instruction que nous avons  indentée après le : est exécutée. Si la condition est fausse, rien ne se
# passe. Notez que les parenthèses utilisées ici avec l’instruction  if sont optionnelles : nous les avons
# utilisées pour améliorer la lisibilité. Dans d’autres langages, il se peut qu’elles soient obligatoires.

# Recommencez encore, en ajoutant deux lignes comme indiqué ci-dessous. Veillez bien à ce que la
# quatrième ligne débute tout à fait à gauche (pas d’indentation), mais que la cinquième soit à nouveau
# indentée (de préférence avec un retrait identique à celui de la troisième) :
# a = 20
# if a > 100:
#     print("a dépasse la centaine")
# else:
#     print("a ne dépasse pas cent")
# <<Exemple 2>>

# Comme vous l’aurez certainement déjà compris, l’instruction  else (« sinon », en anglais) permet de
# programmer  une  exécution  alternative,  dans  laquelle  le  programme  doit  choisir  entre  deux
# possibilités. On peut faire mieux encore en utilisant aussi l’instruction elif(contraction de « else if ») :
# a = 0
# if a > 0:
#     print("a est positif")
# elif a < 0:
#     print("a est négatif")
# else:
#     print("a est nul")
# <<Exemple 3>>

if __name__ == '__main__':
    # <<Exemple 1>>
    # a = 150
    # if a > 100:
    #     print("a dépasse la centaine")
    #     print("a dépasse la centaine")

    # <<Exemple 2>>
    # a = 20
    # if a > 100:
    #     print("a dépasse la centaine")
    # else:
    #     print("a ne dépasse pas cent")

    # <<Exemple 3>>
    a = -1
    if a > 0:
        print("a est positif")
        print("a est positif")
        print("a est positif")
        print("a est positif")
    elif a < 0:
        print("a est négatif")
        print("a est négatif")
        print("a est négatif")
    else:
        print("a est null")
        print("a est null")
        print("a est null")
        print("a est null")

