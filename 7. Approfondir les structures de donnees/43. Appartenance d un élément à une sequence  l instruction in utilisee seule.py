# L’instruction inpeut être utilisée indépendamment de for, pour vérifier si un élément donné fait partie ou
# non  d’une  séquence.  Vous  pouvez  par  exemple  vous  servir  de  in pour  vérifier  si  tel  caractère
# alphabétique fait partie d’un groupe bien déterminé  :
# car = "e"
# voyelles = "aeiouyAEIOUYàâéèêëùîï"
# if car in voyelles:
# print(car, "est une voyelle")

# n = 5
# premiers = [1, 2, 3, 5, 7, 11, 13, 17]
# if n in premiers:
# print(n, "fait partie de notre liste de nombres premiers")
# Cette instruction très puissante effectue donc à elle seule un véritable parcours de la
# séquence. À titre d’ exercice, écrivez les instructions qui effectueraient le même travail à
# l’ aide d’ une boucle classique utilisant l’ instruction while