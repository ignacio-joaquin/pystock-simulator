import matplotlib.pyplot as plt
import random

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def plot(y,nombre):
    plt.plot(x, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Precio')
    plt.title(nombre)
    plt.show(block=False)
    
def IniRandomY(worst,best):
    randomlist = []
    for i in range(0,10):
        n = random.randint(worst,best)
        randomlist.append(n)
    return randomlist

def GuardarY(Y):
    Ystr = ' '.join(map(str, Y))
    with open('y.txt', 'w') as f:
        f.write(Ystr)

def GuardarX(X):
    Xstr = ' '.join(map(str, X))
    with open('x.txt', 'w') as f:
        f.write(Xstr)

Y = IniRandomY(0,50)
GuardarY(Y)
GuardarX(x)
A = 'Inicial'
plot(Y,A)