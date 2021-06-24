import random
matriz=[]
filas = 10#int(input("Introduce numero de filas: "))
columnas= 7#int(input("Introduce numero de columnas: "))   
for i in range(filas):
    for j in range(columnas):
        matriz.append([0]*columnas)
    
for i in range(filas):
    for j in range(columnas):
        matriz[i][j]= round(random.uniform(1,100),2)
    
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j],end="\t")
    print('\n')