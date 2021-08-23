def main():
    #escribe tu código abajo de esta línea
    sal = float(input("Dame el saldo del mes anterior "))
    ing = float(input("Dame los ingresos "))
    egr = float(input("Dame los egresos "))
    chq = int(input("Dame el numero de cheques "))
    r1 = (((sal + ing) - egr) - (chq *13))
    com = r1 * 0.0750
    fin = r1 - com
    print("El resultado es ",fin)

    pass

if __name__ == '__main__':
    main()
