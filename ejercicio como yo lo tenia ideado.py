def calcular_media(listan):
    suma= 0 
    for lista in range(len(listan)):
        x = listan[lista]
        suma += x

    resultado = suma / len(listan)
    print(resultado)



listan = []

cantidad = int(input("Ingrese la cantidad de números de la lista: "))

for x in range(cantidad):
    valor = int(input("Agregue número: "))
    listan.append(valor)

print(calcular_media(listan))