from time import sleep
from turtle import color
import matplotlib.pyplot as plt
import random

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

def plot(y, nombreg):
    plt.plot(x, y, color='blue')
    plt.xlabel('Tiempo')
    plt.ylabel('Precio')
    plt.title(nombreg)
    plt.show(block=False)

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

def GuardarY(Y):
    Ystr = ' '.join(map(str, Y))
    with open('y.txt', 'w') as f:
        f.write(Ystr)

def GuardarX(X):
    Xstr = ' '.join(map(str, X))
    with open('x.txt', 'w') as f:
        f.write(Xstr)

timesSubiendo = 0
timesBajando = 0
timesEstando = 0
z = 0

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
