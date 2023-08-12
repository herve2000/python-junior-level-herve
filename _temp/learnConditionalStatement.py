# petite documentation

# Une instruction conditionnelle en Python est gérée par des instructions if et nous avons vu diverses autres façons
# d'utiliser des instructions conditionnelles comme Python if else ici.
#
# "si condition" - Il est utilisé lorsque vous devez imprimer le résultat lorsque l'une des conditions est vraie ou
# fausse. "autre condition" - il est utilisé lorsque vous souhaitez imprimer la déclaration lorsque votre condition
# ne répond pas à l'exigence "condition elif" - Elle est utilisée lorsque vous avez une troisième possibilité comme
# résultat. Vous pouvez utiliser plusieurs conditions elif pour vérifier les 4 e , 5 e , 6 e possibilités dans votre
# code Nous pouvons utiliser un code minimal pour exécuter des instructions conditionnelles en déclarant toutes les
# conditions dans une seule instruction pour exécuter le code Python If Statement peut être imbriqué

def main():
    a = 1
    b = 2

    # if else
    if a == b:
        print("a est egale a b")
    else:
        print("a est different de b")

    # utiliser else if (elif)
    if a == b:
        print("a est egale a b")
    elif a > b:
        print("a est plus grand que b")
    else:
        print("a est moins grand que b")

    # shicth case
    # python n'a pas de syntaxe swicth case et utilise le mapping
    # des dictionnaire pour l'implementer
    print(switcher(25))


def switcher(elt):
    _dict = {
        0: "cas 0",
        1: "cas 1",
        2: "cas 2"
    }

    return _dict.get(elt, f"L'element {elt} n'existe pas")


if __name__ == '__main__':
    main()
