# En programmation, on appelle  boucle un système d’instructions qui permet de répéter un certain
# nombre de fois (voire indéfiniment) toute une série d’opérations. Python propose deux instructions
# particulières  pour  construire  des  boucles :  l’instruction  for … in … ,  très  puissante,  que  nous
# étudierons plus tard, et l’instruction while que nous allons découvrir tout de suite.
# Veuillez donc entrer les commandes ci-dessous :
# >>> a = 0
# >>> while (a < 7):  # (n’oubliez pas le double point !)
# ... a = a + 1  # (n’oubliez pas l’indentation !)
# ... print(a)
# <<Exemple 1>>

# Exercice
# Ouvrez votre cahier et noter cette série de commandes.
# Décrivez aussi le résultat obtenu, et essayez de l ’expliquer de la manière la
# plus détaillée possible.

# Commentaires

# Le mot  while signifie « tant que » en anglais. Cette instruction utilisée à la seconde ligne indique à
# Python qu’il lui faut répéter continuellement le bloc d’instructions qui suit, tant que le contenu de la variable
# a reste inférieur à 7.

# Comme l’instruction if abordée au chapitre précédent, l’instruction while amorce une instruction  composée.
# Le  double  point  à  la  fin  de  la  ligne  introduit  le  bloc  d ’instructions  à  répéter,  lequel  doit
# obligatoirement se trouver en retrait. Comme vous l’avez appris au chapitre précédent, toutes les instructions
# d’un même bloc doivent être indentées exactement au même niveau (c’est-à-dire décalées à
# droite d’un même nombre d’espaces).

# Nous avons ainsi construit notre première boucle  de  programmation, laquelle répète un certain nombre
# de fois le bloc d’instructions indentées. Voici comment cela fonctionne :
# • Avec l’instruction  while, Python commence par évaluer la validité de la  condition fournie entre
# parenthèses  (celles-ci  sont  optionnelles,  nous  ne  les  avons  utilisées  que  pour  clarifier  notre
# explication).
# • Si la condition se révèle fausse, alors tout le bloc qui suit est ignoré et l ’exécution du programme
# se termine
# • Si la codition est vraie, alors Python exécute tout le bloc d ’instructions constituant  le  corps  de  la
# boucle, c’est-à-dire :
# – l’instruction a = a + 1 qui incrémente d’une unité le contenu de la variable a (ce qui signifie que
# l’on affecte à la variable a une nouvelle valeur, qui est égale à la valeur précédente augmentée
# d’une unité).

# – l’appel de la fonction print() pour afficher la valeur courante de la variable a.
# • lorsque ces deux instructions ont été exécutées, nous avons assisté à une première  itération, et le
# programme boucle, c’est-à-dire que l’exécution reprend à la ligne contenant l’instruction while.
# La condition qui s’y trouve est à nouveau évaluée, et ainsi de suite.

# Dans notre exemple, si la condition a < 7 est encore vraie, le corps de la boucle est exécuté une
# nouvelle fois et le bouclage se poursuit.

# Remarques

# • La variable évaluée dans la condition doit exister au préalable (il faut qu ’on lui ait déjà affecté au
# moins une valeur).
# • Si la condition est fausse au départ, le corps de la boucle n’est jamais exécuté.
# <<Exemple 2>>
# • Si la condition reste toujours vraie, alors le corps de la boucle est répété indéfiniment (tout au
# moins tant que Python lui-même continue à fonctionner). Il faut donc veiller à ce que le corps de
# la boucle contienne au moins une instruction qui change la valeur d ’une variable intervenant dans
# la condition évaluée par while, de manière à ce que cette condition puisse devenir fausse et la
# boucle se terminer.

# Exemple de boucle sans fin (à éviter !) :
# >>> n = 3
# >>> while n < 5:
# ... print("hello !")

# Exercices
# 4.2 Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7.
# 4.3 Ecrire un programme python qui affiche les 100 premiers nombres entiers
# 4.4 Ecrire un programme python qui affiche la somme des cent premiers nombres entiers

# Exercice live (jeux)
# Trouver le bon Chiffre

import time
from random import randrange

if __name__ == '__main__':
    # <<Exemple 1>>
    # a = 1
    # while a < 10:  # (n’oubliez pas le double point !)
    #     print(f"a vaut {a}")
    #     a = a + 1  # (n’oubliez pas l’indentation !)
    #
    # print(f"a vaut {a} final")

    # diskStorage = 500
    # usedDiskStorage = 0
    # pourcentage = 0
    #
    # print("diskStorage vaut ", diskStorage, 'Go')
    # print("usedDiskStorage vaut ", usedDiskStorage, 'Go')
    # print("pourcentage vaut ", pourcentage, '%')
    #
    # while pourcentage < 75:
    #     usedDiskStorage = usedDiskStorage + 50
    #
    #     print("usedDiskStorage vaut ", usedDiskStorage, 'Go')
    #
    #     pourcentage = usedDiskStorage/diskStorage * 100
    #
    #     print("pourcentage vaut ", pourcentage, '%')
    #
    #     time.sleep(4)
    #
    # print(f"sendEmail: ", f"le pourcentage actuelle d'utilisation est : {pourcentage}%", f"l'espace utilise est de {usedDiskStorage}Go")


    # <<Exemple 2>>
    # a = 7
    # while a < 7:
    #     a = a + 1
    #     print(f"ceci ne sera jamais execute")

    # name = 'herve'
    #
    # while name == 'herve':
    #     print('il sagit de l\'utilisateur Herve')

    # Exercice
    # 4.2 Écrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7.

    # print('7*1=7')
    # print('7*1=14')
    # print('7*1=21')
    # print('7*1=28')

    # Exercice live (jeux)
    # Trouver le bon Chiffre

    isFinish = False
    bonChiffre = randrange(1, 10)
    nombreTentative = 10

    print('Bienvenu dans le jeu "Trouver le bon Chiffre"')

    while not isFinish:
        if nombreTentative > 0:
            print('Nombre de tentatives restantes : ', nombreTentative)

            chiffre = int(input("Veuillez entrer le bon chiffre : "))

            nombreTentative = nombreTentative - 1

            if chiffre == bonChiffre:
                isFinish = True
                print('Felicitation, Tu as trouve le bon chiffre qui est : ', chiffre)
            elif chiffre > bonChiffre:
                print('Attention, le chiffre ', chiffre, ' est plus grand que le bon chiffre')
            else:
                print('Attention, le chiffre ', chiffre, ' est plus petit que le bon chiffre')
        else:
            isFinish = True
            print('Game Over')

    print('Fin du Jeu')
