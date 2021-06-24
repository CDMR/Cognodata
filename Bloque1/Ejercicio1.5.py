import random
import numpy as np
from numpy.core.numeric import normalize_axis_tuple
vector=[]
normal=[]
for j in range(10):
        vector.append([0]*10)
        vector[j]= round(random.uniform(1,100),2)
numeros=np.array(vector)
media=np.mean(numeros)
desviacion=np.std(numeros)
caracter=str(numeros)

for j in range(10):
        normal.append([0]*10)
        normal[j]= (vector[j]-media)/desviacion
normalizado=np.array(normal)
print(numeros,normalizado)
selecval=normalizado[np.where((normalizado <= 1) & (normalizado >= -1))]
estructura=[numeros,caracter]
print(sorted(selecval))