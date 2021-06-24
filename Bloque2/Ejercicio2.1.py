import random
import numpy as np
import pandas as pd

arreglo1=np.random.randint(1,11,(1,100))
arreglo2=np.random.randint(11,21,(1,100))
frec568=[np.count_nonzero(arreglo1==5),np.count_nonzero(arreglo1==6), np.count_nonzero(arreglo1==8)]
frec141619=[np.count_nonzero(arreglo2==14),np.count_nonzero(arreglo2==16), np.count_nonzero(arreglo2==19)]
print ([[5,6,8],frec568],[[14,16,19],frec141619])