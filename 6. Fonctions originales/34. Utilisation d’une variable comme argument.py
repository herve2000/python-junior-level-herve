# Dans les 2 exemples qui précèdent, l’argument que nous avons utilisé en appelant la fonction  table() était à
# chaque fois une constante (la valeur 13, puis la valeur 9). Cela n’est nullement obligatoire.
# L ’argument que nous  utilisons dans l’appel d’une fonction peut être une variable lui aussi, comme dans l’exemple
# ci-dessous.
# Analysez bien  cet  exemple,  essayez-le  concrètement,  et  décrivez  le  mieux possible dans votre cahier
# d’exercices ce que vous obtenez, en expliquant avec vos propres mots ce qui se passe.
# Cet exemple devrait vous donner un premier aperçu de l’utilité des fonctions pour accomplir simplement des tâches
# complexes
# >>> a = 1
# >>> while a <20:
# ... table(a)
# ... a = a +1
# ...
# <<Exemple 1>>

# Remarque importante Dans l’exemple ci-dessus, l’argument que nous passons à la fonction
# table() est le contenu de la variable a. À l’intérieur de la fonction, cet argument est affecté au paramètre  base,
# qui est une tout autre variable. Notez donc bien dès à présent que Ces  noms peuvent être identiques si vous
# le voulez, mais vous  devez  bien comprendre  qu ’ils  ne désignent pas
# la même chose (en dépit du fait qu’ils puissent éventuellement contenir une valeur identique).
#
# Exercice 7.1
# Importez le module turtle pour pouvoir effectuer des dessins simples. Vous allez dessiner une série de triangles
# équilatéraux de différentes couleurs. Pour ce faire, définissez d’abord une fonction triangle() capable de dessiner
# un triangle d’une couleur  bien  déterminée  (ce  qui  signifie  donc  que  la  définition  de  votre  fonction
# doit comporter un paramètre pour recevoir le nom de cette couleur). Utilisez ensuite cette fonction pour reproduire
# ce même triangle en différents endroits, en changeant de couleur à chaque fois.

from turtle import *
from time import *


def table(base):
    print("Table de multiplication par", base)
    n = 1
    while n < 11:
        print(n * base, end=' ')
        n = n + 1
    print("\n")


def exercise7_1():
    triangle("green")
    triangle("red")
    triangle("yellow")


def triangle(ferdinand_color):
    color(ferdinand_color)
    forward(100)
    sleep(2)
    left(120)
    forward(100)
    sleep(2)
    left(120)
    forward(100)
    left(120)
    sleep(5)

    move()


def move():
    up()
    forward(150)
    down()


if __name__ == '__main__':
    # <<Exemple 1>>
    # a = 1
    # while a < 20:
    #     table(a)
    #     a = a + 1

    exercise7_1()
