# Les scripts que vous avez écrits jusqu’à présent étaient à chaque fois très courts, car leur objectif était
# seulement de vous faire assimiler les premiers éléments du langage. Lorsque vous commencerez à
# développer de véritables projets, vous serez confrontés à des problèmes souvent fort complexes, et les
# lignes de programme vont commencer à s’accumuler...
# L’approche  efficace  d’un  problème  complexe  consiste  souvent  à  le  décomposer  en  plusieurs
# sous-problèmes  plus  simples  qui  seront  étudiés  séparément  (ces  sous-problèmes  peuvent
# éventuellement être eux-mêmes décomposés à leur tour, et ainsi de suite). Or il est important que
# cette décomposition soit représentée fidèlement dans les algorithmes pour que ceux-ci restent clairs.

# D’autre part, il arrivera souvent qu’une même séquence d’instructions doive être utilisée à plusieurs
# reprises  dans  un  programme,  et  on  souhaitera  bien  évidemment  ne  pas  avoir  à  la  reproduire
# systématiquement. et  les  classes  d’objets sont  différentes  structures  de  sous-programmes  qui  ont  été
# imaginées par les concepteurs des langages de haut niveau afin de résoudre les difficultés évoquées
# ci-dessus. Nous allons commencer par décrire ici la définition  de  fonctions sous Python. Les objets et les
# classes seront examinés plus loin.
# Nous  avons  déjà  rencontré  diverses  fonctions  pré-programmées.  Voyons  à  présent  comment  en
# définir nous-mêmes de nouvelles.
# La syntaxe Python pour la définition d’une fonction est la suivante :
# def nomDeLaFonction(liste de paramètres):
#      ...
#      bloc d'instructions
#      ...
# <<Exemple 1>>

# • Vous pouvez choisir n’importe quel nom pour la fonction que vous créez, à l ’exception des mots
# réservés du  langage et  à  la  condition  de  n ’utiliser aucun  caractère  spécial  ou  accentué (le
# caractère souligné « _ » est permis). Comme c’est le cas pour les noms de variables, il vous est
# conseillé  d’utiliser  surtout  des  lettres  minuscules,  notamment  au  début  du  nom  (les  noms
# commençant par une majuscule seront réservés aux classes que nous étudierons plus loin).

# • Comme les instructions if et while que vous connaissez déjà, l’instruction def est une instruction
# composée. La ligne contenant cette instruction se termine obligatoirement par un double point,
# lequel introduit un bloc d’instructions que vous ne devez pas oublier d’indenter.

# • La liste  de  paramètres spécifie quelles informations il faudra fournir en guise  d’arguments lorsque
# l’on  voudra  utiliser  cette  fonction  (les  parenthèses  peuvent  parfaitement  rester  vides  si  la
# fonction ne nécessite pas d’arguments).

# • Une  fonction  s’utilise  pratiquement  comme  une  instruction  quelconque.  Dans  le  corps  d ’un
# programme, un appel de fonction est constitué du nom de la fonction suivi de parenthèses.
# Si  c’est  nécessaire,  on  place  dans  ces  parenthèses  le  ou  les  arguments  que  l’on  souhaite
# transmettre à la fonction. Il faudra en principe fournir un argument pour chacun des paramètres
# spécifiés dans la définition de la fonction, encore qu ’il soit possible de définir pour ces paramètres
# des valeurs par défaut (voir plus loin).

# <<Exemple 1>>
def salut():
    print("Hello world!")


def auRevoir(name):
    print("Good bye", name)


def saluts(firstPerson, secondPerson):
    print(f"Salut {firstPerson} et {secondPerson}")


if __name__ == '__main__':
    # <<Exemple 1>>
    # salut()

    # auRevoir("Ferdinand")
    # auRevoir("Lucas")
    # auRevoir("Elvira")

    saluts(firstPerson="Herve", secondPerson="Jordan")
    saluts(secondPerson="Jordan", firstPerson="Herve")
