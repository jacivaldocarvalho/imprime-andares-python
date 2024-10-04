def imprimir_andares_while():
    andar = 20
    while andar > 0:
        if andar != 13:
            print(andar)
        andar -= 1


def imprimir_andares_do_while():
    andar = 20
    while True:
        if andar != 13:
            print(andar)
        andar -= 1
        if andar <= 0:
            break


def imprimir_andares_for():
    for andar in range(20, 0, -1):
        if andar != 13:
            print(andar)


def main():
    print("Usando laço for:")
    imprimir_andares_for()
    print("\nUsando laço while:")
    imprimir_andares_while()
    print("\nUsando laço do while:")
    imprimir_andares_do_while()


if __name__ == "__main__":
    main()
