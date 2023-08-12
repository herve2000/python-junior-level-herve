if __name__ == '__main__':
    # while loop
    x = 0

    while x < 4:
        print(f"x vaut {x}")
        x += 1

    # for loop
    y = 0

    for y in range(2, 7):
        print(f"y vaut {y}")

    # break statement in for loop
    for y in range(10, 20):
        print(f"y vaut {y}")

        if y == 15:
            break

    # continue statement for loop
    for z in range(10, 20):
        if z % 5 == 0:
            continue
        print(f"z vaut {z}")
