if __name__ == '__main__':
    # simple
    # print("Helloworld ")

    # avec une valeur passee en parametre
    # b = 20
    # print(f"b vaut: {b}")

    # concatenation
    # a = "Bonjour"
    # b = " à tous"
    # print(a+b)

    # concatenation avec different type (on converti en string)
    a = "Herve "
    b = 2000

    print(f"type de a {type(a)}")
    print(f"type de b {type(b)}")

    b = str(b)

    print(f"type de b {type(b)}")

    print(a+b)
