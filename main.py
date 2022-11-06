import matplotlib.pyplot as plt
import random
from time import sleep
from turtle import color

i = 0
new_saldo = 0
Tieneacc = 0
timesSubiendo = 0
timesBajando = 0
timesEstando = 0
z = 0
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def Decididor(Tendencia, timesSubiendo, timesEstando, timesBajando): # 1 = crece, 0 = se mantiene, -1 = baja
    chances = random.randint(0,100)
    
    if Tendencia > 0: #si aumenta
        timesEstando = 0
        timesBajando = 0
        if timesSubiendo == 0:
            if chances < 41 :
                timesSubiendo = timesSubiendo+1                
                return 1
        
            if chances >= 41 and chances <= 70:
                return 0
        
            if chances > 70 :
                return -1
        
        if timesSubiendo == 1:
            if chances < 31 :
                timesSubiendo = timesSubiendo+1                
                return 1
        
            if chances >= 31 and chances <= 70 :
                return 0
        
            if chances > 70 :
                return -1 

        if timesSubiendo > 1:
            if chances < 21 :
                timesSubiendo = timesSubiendo+1               
                return 1
        
            if chances >= 21 and chances <= 60 :
                return 0
        
            if chances > 60 :
                return -1                       

    if Tendencia == 0: #si viene igual
        timesBajando = 0
        timesSubiendo = 0
        if timesEstando == 0:
            if chances < 31 :
                return 1
        
            if chances >= 31 and chances <= 70:
                timesEstando = timesEstando+1                
                return 0
        
            if chances > 70 :
                return -1         

        if timesEstando > 0:
            if chances < 41 :
                return 1
        
            if chances >= 41 and chances <= 60:
                timesEstando = timesEstando+1
                return 0
        
            if chances > 60 :
                return -1   

    if Tendencia < 0: #si baja    
        timesEstando = 0
        timesSubiendo = 0
        if timesBajando == 0:
            if chances < 36:
                timesBajando = timesBajando+1                
                return -1
        
            if chances >=36 :
                return 0   
        
        if timesBajando == 1:
            if chances < 36:              
                return 0
        
            if chances >=36 :
                timesBajando = timesBajando+1                
                return -1              

        if timesBajando > 1:
            if chances < 50:              
                return 0
        
            if chances >= 50 :
                timesBajando = timesBajando+1                
                return -1              

def AvanzadorY(list, Tendencia, timesSubiendo, timesEstando, timesBajando):
    list.pop(0)
    d = Decididor(Tendencia, timesSubiendo, timesEstando, timesBajando)
    if d > 0:
        a = list[8]+1
        b = list[8]+5
        n = random.randint(a, b)
        list.append(n)
    if d == 0:
        n = list[8]
        list.append(n)
    if d < 0:
        a = list[8]-1
        while a < 0:
            a=a+1
        b = list[8]-5
        while b < 0:
            b=b+1
        n = random.randint(b, a)
        list.append(n)

def AvanzadorX(list):
    list.pop(0)
    n = list[8]
    list.append(n+1)
    return list

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

def LectorY():
    my_file = open("y.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    return new_char

def LectorX():
    my_file = open("x.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    return new_char

def refresh(z):
    Y = LectorY()
    B = 'b'
    o = LectorX()
    Tendencia = Y[4] - Y[3]
    AvanzadorY(Y, Tendencia, timesSubiendo, timesEstando, timesBajando)
    x = AvanzadorX(o)
    GuardarY(Y)
    GuardarX(x)
    plot(Y,B)
    z = z+1


def comprar(saldo, num):
    my_file = open("y.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    saldo = saldo - new_char[9] * num
    return saldo

def vender(saldo, num):
    my_file = open("y.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    saldo = saldo + new_char[9] * num
    return saldo 

def acc(saldo, Tieneacc):
    while True:
        print("Desea comprar, vender, o pasar?")
        a = input()
        if a == "comprar":
            print("Cuantas acciones?")
            num = input()
            accionval = LectorY()
            if(saldo >= int(num) * accionval[9]):
                saldo = comprar(saldo, int(num))
                Tieneacc = int(num)
                return saldo, Tieneacc
            else:
                print("Saldo insuficiente, pruebe con menos acciones")
        if a == "vender" and Tieneacc >= 1:
            saldo = vender(saldo, Tieneacc)
            Tieneacc = 0
            return saldo, Tieneacc
        if a == "pasar":
            return saldo, Tieneacc
        if a == "vender" and Tieneacc == 0:
            print("Usted no tiene acciones para vender")        
        else:
            print("Comando desconocido")

def ini():
    Y = IniRandomY(0,50)
    GuardarY(Y)
    GuardarX(x)
    A = 'Inicial'
    plot(Y,A)





print("--------------------------------------------------")
print("-               Simulador de bolsa               -")
print("-               By Ignacio Joaquin               -")
print("--------------------------------------------------")
print(" ")
print(" ")
print("Tiene un saldo de $100")
saldo = 100

ini()
while i==0:
    saldo, Tieneacc = acc(saldo, Tieneacc)
    print("Saldo restante " + str(saldo))
    plt.close()
    refresh(z)