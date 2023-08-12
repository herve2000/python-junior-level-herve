# Les noms de variables sont des noms que vous choisissez vous-même assez librement. Efforcez-vous
# cependant  de bien les choisir : de préférence assez courts,  mais aussi  explicites que  possible, de
# manière à exprimer clairement ce que la variable est censée contenir. Par exemple, des noms de
# variables tels que altitude, altit ou alt conviennent mieux que x pour exprimer une altitude.

# Un bon programmeur doit veiller à ce que ses lignes d’instructions soient faciles à lire.
# Sous Python, les noms de variables doivent en outre obéir à quelques règles simples :

# • Un nom de variable est une séquence de lettres (a → z , A → Z) et de chiffres (0  → 9), qui doit
# toujours commencer par une lettre.
# <<Exemple 1>>

# • Seules les lettres ordinaires sont autorisées. Les lettres accentuées, les cédilles, les espaces, les
# caractères spéciaux tels que $, #, @, etc. sont interdits, à l’exception du caractère _ (souligné).
# <<Exemple 2>>

# • La casse est significative (les caractères majuscules et minuscules sont distingués).
# Attention : Joseph, joseph, JOSEPH sont donc des variables différentes.
# <<Exemple 3>>

# Soyez attentifs  ! Prenez l’habitude d’écrire l’essentiel des noms de variables en
# caractères minuscules (y compris la première lettre)
# Il s’agit d’une simple convention, mais elle est largement respectée. N ’utilisez les
# majuscules qu’à l’intérieur même du nom, pour en augmenter éventuellement la lisibilité, comme dans
# tableDesMatieres.
# <<Exemple 4>>

# En plus de ces règles, il faut encore ajouter que vous ne pouvez pas utiliser comme nom de variables
# les 33 « mots réservés » ci-dessous (ils sont utilisés par le langage lui-même) :
# and as assert break class continue def
# del elif else except False finally for
# from global if import in is lambda
# None nonlocal not or pass raise return
# True try while with yield
# <<Exemple 5>>

if __name__ == '__main__':
    # <<Exemple 1>>
    # variable commencant par un chiffre
    # 2emePerson = 56
    person2 = 56

    # << Exemple 2 >>
    # caractere speciaux interdit
    # herve@gmail = 56

    # exception du carractere _
    # herve_2000 = 56
    # print(f"herve_2000 vaut : {herve_2000}")

    # << Exemple 3 >>
    # Joseph = 1
    # joseph = 2
    # JOSEPH = 3
    # print(f" Joseph vaut {Joseph} \n joseph vaut {joseph} \n JOSEPH vaut {JOSEPH}")

    # <<Exemple 4>>
    # deconseille pour les nom de variable
    # TableDesMatieres = 56
    # TABLEDESMATIERES = 56
    # conseille
    # tableDesMatieres = 56

    # <<Exemple 5>>
    # global = 20
    # for = 50
    # from = 56
