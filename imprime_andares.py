def imprimir_andares_while(andar):
    andar = andar
    while andar > 0:
        if andar != 13:
            print(andar)
        andar -= 1


def imprimir_andares_do_while(andar):
    andar = andar
    while True:
        if andar != 13:
            print(andar)
        andar -= 1
        if andar <= 0:
            break


def imprimir_andares_for(andar):
    for andar in range(andar, 0, -1):
        if andar != 13:
            print(andar)


def main():

    andar = 21

    print("\nUsando laço while:")
    imprimir_andares_while(andar)
    print("\nUsando laço do while:")
    imprimir_andares_do_while(andar)
    print("Usando laço for:")
    imprimir_andares_for(andar)


if __name__ == "__main__":
    main()
