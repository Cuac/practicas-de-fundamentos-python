import random
#se necesita el comando python -m pip install -U pip
#python -m pip install -U matplotlip
import matplotlib.pyplot as plt
#numero alearotio
print(random.randrange(10,200, 2))

#reacomodar una lista al azar
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('lista original', lista)
random.shuffle(lista)
print('Nueva lista', lista)

campana = [random.gauss(1, 0.5) for i in range(1000)]
plt.hist(campana, bins=25)
plt.show()