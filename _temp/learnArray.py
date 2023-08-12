# petite documentation
# on utile un tableau quand on a besoin de stocker une grande
# quantite de donne de meme type ou une collection d'objet.
# l'utilisation de tableau utilise moins de memoire que
#  les listes
#
# le type du tableau memo
# Tapez le code Type Python Type C Taille minimale (octets)
# 'tu' Caractère Unicode Py_UNICODE 2
# 'b' Int Caractère signé 1
# 'B' Int Caractère non signé 1
# 'h' Int Court signé 2
# 'l' Int Signé longtemps 4
# 'L' Int Long non signé 4
# 'q' Int Signé long long 8
# 'Q' Int Non signé long long 8
# 'H' Int Court non signé 2
# 'F' Flotteur Flotteur 4
# 'ré' Flotteur Double 8
# 'je' Int Signé en 2
# 'JE' Int Entier non signé 2

# Un tableau est un type courant de structure de données dans lequel tous les éléments doivent être du même type de
# données. La programmation Python , un tableau, peut être gérée par le module « tableau ». Les tableaux Python sont
# utilisés lorsque vous devez utiliser de nombreuses variables du même type. En Python, les éléments de tableau sont
# accessibles via des indices. Les éléments de tableau peuvent être insérés à l'aide d'une syntaxe array.insert(i,
# x). En Python, les tableaux sont modifiables. En Python, un développeur peut utiliser la méthode pop() pour faire
# apparaître un élément du tableau Python. Le tableau Python peut être converti en Unicode. Pour répondre à ce
# besoin, le tableau doit être de type 'u' ; sinon, vous obtiendrez "ValueError". Les tableaux Python sont différents
# des listes. Vous pouvez accéder à n'importe quel élément du tableau en utilisant son index. Le module tableau de
# Python a des fonctions distinctes pour effectuer des opérations sur les tableaux.

import array


def main():
    # declarer
    _array = array.array("i")

    # insertion d'element
    _array.insert(0, 25)

    # declarer en initialisant un tableau
    _array1 = array.array("i", [1, 2, 3])

    # modifier une valeur
    _array[0] = 75

    # acceder a un element via son index
    print(_array[0])

    # suprimer un element d'un tableau
    # _oo = _array.pop(0)

    # on peut aussi utiliser del
    del _array[0]

    print(_array)

    # suprimer une valeur d'un tableau
    _array1.remove(1)

    print(_array1)

    # recuperer l'index d'une valeur
    print(f"l'index de 3 dans le tableau _array1 est {_array1.index(3)}")

    # renverser un tableau
    print(f"voici le tableau _array1 {_array1}")
    print("on le renverse")
    _array1.reverse()
    print(f"voici le tableau _array1 {_array1}")

    # taille du tableau
    print(f"la taille du tableau _array1 est {len(_array1)}")

    # nombre d'aucurence d'une valeur
    _array1.insert(2, 3)
    print(f"le nombre d'occurence de la valeur 3 dans le tableau _array1 est {_array1.count(3)}")


if __name__ == '__main__':
    main()
