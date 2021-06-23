import random
import numpy as np
vector=[]
for j in range(10):
        vector.append([0]*10)
        vector[j]= round(random.uniform(1,100),2)
numeros=np.array(vector)
caracter=str(numeros)
estructura=[numeros,caracter]
print(estructura)