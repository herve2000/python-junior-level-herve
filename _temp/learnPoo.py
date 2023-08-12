# petite documentation

# « Classe » est un regroupement logique de fonctions et de données. La classe Python fournit toutes les
# fonctionnalités standard de la programmation orientée objet.
#
# Mécanisme d'héritage de classe Une classe dérivée qui remplace toute méthode de sa classe de base Une méthode peut
# appeler la méthode d'une classe de base portant le même nom Les classes Python sont définies par le mot clé "class"
# lui-même À l'intérieur des classes, vous pouvez définir des fonctions ou des méthodes qui font partie de la classe
# Tout dans une classe est indenté, tout comme le code dans la fonction, la boucle, l'instruction if, etc. L'argument
# self en Python fait référence à l'objet lui-même. Self est le nom préféré par convention par Pythons pour indiquer
# le premier paramètre des méthodes d'instance en Python Le runtime Python transmettra automatiquement la valeur
# "self" lorsque vous appelez une méthode d'instance sur in instance, que vous la fournissiez délibérément ou non En
# Python, une classe peut hériter des attributs et des méthodes de comportement d'une autre classe appelée
# sous-classe ou classe héritière.

def main():
    person = Person("Franck")

    person.showName()

    director = Director("Herve")

    director.showName()

    director.punish()


class Person:

    name = ""

    def __init__(self, name):
        self.name = name

    def showName(self):
        print(f"my name is {self.name}")


class Director(Person):

    def punish(self):
        print(f"me {self.name} i can punish you")


if __name__ == '__main__':
    main()
