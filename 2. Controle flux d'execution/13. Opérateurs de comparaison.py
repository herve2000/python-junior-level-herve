# La condition évaluée après l’instruction if peut contenir les opérateurs de comparaison suivants :
# x == y  # x est égal à y
# x != y  # x est différent de y
# x > y  # x est plus grand que y
# x < y  # x est plus petit que y
# x >= y  # x est plus grand que, ou égal à y
# x <= y  # x est plus petit que, ou égal à y

# a = 7
#     if a % 2 == 0:
#         print("a est pair")
#         print("parce que le reste de sa division par 2 est nul")
#     else:
#         print("a est impair")
# <<Exemple 1>>

# Notez bien que l’opérateur de comparaison pour l’égalité de deux valeurs est constitué de deux signes
# « égale » et non d’un seul
# Le signe « égale » utilisé seul est un opérateur d’affectation, et non un
# opérateur de comparaison. Vous retrouverez le même symbolisme en C++ et en Java.

if __name__ == '__main__':
    # <<Exemple 1>>
    a = 6
    amodulo2 = a % 2
    print("amodulo2 -->", amodulo2)
    if amodulo2 == 0:
        print("a est pair")
        print("parce que le reste de sa division par 2 est nul")
    else:
        print("a est impair")

    # difference
    # a = 12
    # if a != 12:
    #     print("a est different de 12")

    # superiur ou egale
    # a = 19
    # if a >= 19:
    #     print("a est soit superieur soit egale a 19")
    #     if a == 19:
    #         print("a est egale a 19")
    #
    #         print("a est egale a 19")
    #
    #     if a > 19:
    #         print("a est superieur a 19")
    #
    # print("on continue comme si de rien etait")

    # tailleFichier = 7
    #
    # if tailleFichier <= 5:
    #     print("bloc 1")
    #     print("supression")
