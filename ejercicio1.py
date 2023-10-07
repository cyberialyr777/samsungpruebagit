
x = 0


listaImpar=[]

while x == 0:
    numero = int(input('escriba un numero positivo: '))
        
    if numero > 0:
        for x in range(1,numero):
            resultado = 0
            resultado = x % 2
            
            if resultado != 0:
                listaImpar.append(x)

        x = 1

print(listaImpar)
    

            