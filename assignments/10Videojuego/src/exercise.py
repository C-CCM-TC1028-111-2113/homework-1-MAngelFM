def main():
    #escribe tu código abajo de esta línea
    vid = int(input("Dame el numero de Juegos Nuevos "))
    uss = int(input("Dame la cantidad de Juegos Usados "))

    vid1 = vid*1000
    uss1 = uss*350
    tot = vid1 + uss1

    print("El total es ",tot)



if __name__ == '__main__':
    main()
