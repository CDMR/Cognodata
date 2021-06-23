import random
import pandas as pd
matriz=[]
filas = 10
columnas= 7   
    
for i in range(filas):
    matriz.append([0]*columnas)
    for j in range(columnas):
        matriz[i][j]= round(random.uniform(0,100),2)

dias=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
df= pd.DataFrame(data=matriz, columns=dias)
print(matriz)
print(df)