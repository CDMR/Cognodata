import random
import numpy as np
vector=[]
normalizado=[]
for j in range(10):
        vector.append([0]*10)
        vector[j]= round(random.uniform(1,100),2)
numeros=np.array(vector)
media=np.mean(numeros)
desviacion=np.std(numeros)
caracter=str(numeros)

for j in range(10):
        normalizado.append([0]*10)
        normalizado[j]= (vector[j]-media)/desviacion
estructura=[numeros,caracter]
print(numeros,normalizado)