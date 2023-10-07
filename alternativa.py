def calcular_promedio(x):
    suma=0
    for i in x:
        suma += i
    promedio = suma / len(x)
    print(promedio,"\n",x)
        
        
mi_lista = []    
num_lista = int(input("Cantidad de números a ingresar: "))

for i in range(num_lista):
    numero = int(input("Ingrese el número: "))
    mi_lista.append(numero)

calcular_promedio(mi_lista)