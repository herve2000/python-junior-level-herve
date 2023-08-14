# La plupart des scripts élaborés nécessitent à un moment ou l ’autre une intervention de l’utilisateur
# (entrée d’un paramètre, clic de souris sur un bouton, etc.).
# Dans un script en mode texte (comme ceux que nous  avons créés jusqu’à présent), la méthode la plus simple
# consiste à employer la fonction intégrée input().
# Cette fonction provoque une interruption dans le programme courant. L ’utilisateur
# est invité à entrer des  caractères au clavier et à  terminer avec <Enter>.
# Lorsque cette touche est enfoncée, l’exécution du  programme se poursuit,  et la fonction fournit en retour
# une  chaîne de caractères correspondant à ce que l’utilisateur a saisi. Cette chaîne peut alors être assignée à une
# variable quelconque, convertie, etc.

# On peut invoquer la fonction  input() en laissant les parenthèses vides. On peut aussi y placer en
# argument un message explicatif destiné à l’utilisateur.
# Exemple :
# prenom = input("Entrez votre prénom : ")
# print("Bonjour,", prenom)
# <<Exemple 1>>

# ou encore :
# print("Veuillez entrer un nombre positif quelconque : ", end=" ")
# ch = input()
# nn = int(ch)  # conversion de la chaîne en un nombre entier
# print("Le carré de", nn, "vaut", nn**2)
# Soulignons que la fonction input() renvoie toujours une chaîne de caractères
# <<Exemple 2>>

# Si vous souhaitez que l’utilisateur entre une valeur numérique, vous devrez donc convertir la valeur entrée
# (qui sera donc de toute façon de type string) en une valeur numérique du type qui vous convient, par l’intermédiaire
# des  fonctions  intégrées  int() (si  vous  attendez  un  entier)  ou  float() (si  vous  attendez  un  réel).
# Exemple :
# >>> a = input("Entrez une donnée numérique : ")
# Entrez une donnée numérique : 52.37
# >>> type(a)
# <class 'str'>
# >>> b = float(a)   # conversion de la chaîne en un nombre réel
# >>> type(b)
# <class 'float'>
# <<Exemple 3>>


if __name__ == '__main__':
    # <<Exemple 1>>  nom_de_la_fonction()
    # prenom = input("Entrez votre prénom : ")
    # print("Bonjour,", prenom)

    # <<Exemple 2>>
    # nombrePositifString = input("Veuillez entrer un nombre positif quelconque : ")
    # print("type(nombrePositifString)-->", type(nombrePositifString), "valeur", nombrePositifString)
    # nombrePositifInt = int(nombrePositifString)  # conversion de la chaîne en un nombre entier
    # print("type(nombrePositifInt)-->", type(nombrePositifInt), "valeur", nombrePositifInt)
    #
    # print("Le carré de", nombrePositifInt, "vaut", nombrePositifInt**2)

    # <<Exemple 3>>
    # a = input("Entrez une donnée numérique : ")
    #
    # print("le type du nombre que vous avez entrez est ", type(a), " Ce nombre vaut ", a)
    #
    # b = float(a)   # conversion de la chaîne en un nombre réel
    #
    # print("le type du nombre que vous avez entrez apres sa conversion est ", type(b), " Ce nombre vaut ", b)

