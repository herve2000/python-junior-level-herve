# Il est parfaitement possible d’imbriquer les unes dans les autres plusieurs instructions composées, de
# manière à réaliser des structures de décision complexes. Exemple :
# if embranchement == "vertébrés":
#     if classe == "mammifères":
#         if ordre == "carnivores":
#             if famille == "félins":
#                 print("c’est peut-être un chat")
#             print("c’est en tous cas un mammifère")
#     elif classe == "oiseaux":
#         print("c’est peut-être un canari")
# print("la classification des animaux est complexe")
# <<Exemple 1>>

# Analysez cet exemple. Ce fragment de programme n’imprime la phrase « c’est peut-être un chat » que
# dans le cas où les quatre premières conditions testées sont vraies.
# Pour que la phrase « c’est en tous cas un mammifère » soit affichée, il faut et il suffit que les deux
# premières conditions soient vraies. L’instruction d’affichage de cette phrase (ligne 4) se trouve en effet
# au même niveau d’indentation que l’instruction :  if ordre == "carnivores": (ligne 3). Les deux font
# donc partie d’un même bloc, lequel est entièrement exécuté si les conditions testées aux lignes 1 et 2
# sont vraies.

# Pour que la phrase « c’est peut-être un canari » soit affichée, il faut que la variable  embranchement
# contienne « vertébrés », et que la variable classe contienne « oiseaux ».
# Quant à la phrase de la ligne 9, elle est affichée dans tous les cas, parce qu ’elle fait partie du même bloc
# d’instructions que la ligne 1

if __name__ == '__main__':
    # <<Exemple 1>>
    embranchement = "vertébrés"
    classe = "mammifères"
    ordre = "carnivores"
    famille = "félins"

    if embranchement == "vertébrés":  # 1
        if classe == "mammifères":  # 2
            if ordre == "carnivores":  # 3
                if famille == "félins":  # 4
                    print("c’est peut-être un chat")  # 5
                print("c’est en tous cas un mammifère")  # 6
        elif classe == "oiseaux":  # 7
            print("c’est peut-être un canari")  # 8
    print("la classification des animaux est complexe")  # 9
