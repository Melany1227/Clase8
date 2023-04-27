def sumar_5_enteros():
    lista = []
    contador = 0
    tam = 5
    suma = 0

    while contador < tam:
        lista.append(int(input("Ingrese número " + str(contador+1) + ": ")))
        contador += 1

    contador = 0
    while contador < tam:
        suma += lista[contador]
        contador += 1

    print("Los números de la lista son: ")
    for numero in lista:
        print(numero, end=', ')

    print("\nLa suma de todos sus elementos es:")
    print(suma)