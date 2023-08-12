
def start():
    # acceder a une variable globale
    global a

    # modifier une variable globale
    a = "a modifie"
    print(f"start::: a vaut: {a}")

    b = "b modifie"
    print(f"start::: b vaut: {b}")


if __name__ == '__main__':
    a = "a initial"
    b = "b initial"

    print(f"main::: a vaut: {a}")
    print(f"main::: b vaut: {b}")

    start()

    print(f"main::: a vaut: {a}")
    print(f"main::: b vaut: {b}")
