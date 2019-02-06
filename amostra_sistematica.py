import numpy as np
import pandas as pd
from math import ceil

populacao = 150
amostra = 15

k = ceil(populacao/amostra)

r = np.random.randint(low=1, high= k +1, size = 1)

acumulador = r[0]
sorteados = []

for _ in range(amostra):
	#print(acumulador)
	sorteados.append(acumulador)
	acumulador += k
print(k)
print(r)
print(sorteados)