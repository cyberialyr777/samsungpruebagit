import random as rd

listan = []

cantidad = int(input("Ingrese la cantidad de números de la lista: "))

for x in range(cantidad):
    valor = int(input("Agregue número: "))
    listan.append(valor)

def calcular_media(listan):
    suma= 0
    for i in listan:
        x = listan[i]
        suma += x
    resultado = suma / len(listan)

calcular_media(listan)