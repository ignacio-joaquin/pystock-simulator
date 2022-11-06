import matplotlib.pyplot as plt
import random
from time import sleep
from turtle import color

i = 0
new_saldo = 0
hasacc = 0
timesUp = 0
timesDown = 0
timesFrezze = 0
z = 0
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def Decider(Tendency, timesUp, timesFrezze, timesDown): # This fuction decides if the graph goes up, down or flat. 1 for up, 0 for flat, -1 for down.
    odds = random.randint(0,100)
    
    if Tendency > 0: #if tendency is to go up
        timesFrezze = 0
        timesDown = 0
        if timesUp == 0:
            if odds < 41 :
                timesUp = timesUp+1                
                return 1
        
            if odds >= 41 and odds <= 70:
                return 0
        
            if odds > 70 :
                return -1
        
        if timesUp == 1:
            if odds < 31 :
                timesUp = timesUp+1                
                return 1
        
            if odds >= 31 and odds <= 70 :
                return 0
        
            if odds > 70 :
                return -1 

        if timesUp > 1:
            if odds < 21 :
                timesUp = timesUp+1               
                return 1
        
            if odds >= 21 and odds <= 60 :
                return 0
        
            if odds > 60 :
                return -1                       

    if Tendency == 0: #if tendency is to go flat
        timesDown = 0
        timesUp = 0
        if timesFrezze == 0:
            if odds < 31 :
                return 1
        
            if odds >= 31 and odds <= 70:
                timesFrezze = timesFrezze+1                
                return 0
        
            if odds > 70 :
                return -1         

        if timesFrezze > 0:
            if odds < 41 :
                return 1
        
            if odds >= 41 and odds <= 60:
                timesFrezze = timesFrezze+1
                return 0
        
            if odds > 60 :
                return -1   

    if Tendency < 0: #if tendency is to go down   
        timesFrezze = 0
        timesUp = 0
        if timesDown == 0:
            if odds < 36:
                timesDown = timesDown+1                
                return -1
        
            if odds >=36 :
                return 0   
        
        if timesDown == 1:
            if odds < 36:              
                return 0
        
            if odds >=36 :
                timesDown = timesDown+1                
                return -1              

        if timesDown > 1:
            if odds < 50:              
                return 0
        
            if odds >= 50 :
                timesDown = timesDown+1                
                return -1              

def AvanzadorY(list, Tendency, timesUp, timesFrezze, timesDown): #this fuction will update the list whit the stock value
    list.pop(0)
    d = Decider(Tendency, timesUp, timesFrezze, timesDown)
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

def AvanzadorX(list): #this fuction will update the list whit the time value
    list.pop(0)
    n = list[8]
    list.append(n+1)
    return list

def plot(y,nombre): #this fuction plots the graph
    plt.plot(x, y)
    plt.xlabel('Tiempo')
    plt.ylabel('Precio')
    plt.title(nombre)
    plt.show(block=False)
   
def IniRandomY(worst,best): #this fuction just make a random list to start the first graph
    randomlist = []
    for i in range(0,10):
        n = random.randint(worst,best)
        randomlist.append(n)
    return randomlist

def SaveY(Y): #this fuction saves y values
    Ystr = ' '.join(map(str, Y))
    with open('y.txt', 'w') as f:
        f.write(Ystr)

def SaveX(X): #this fuction saves x values
    Xstr = ' '.join(map(str, X))
    with open('x.txt', 'w') as f:
        f.write(Xstr)

def ReaderY(): #this fuction reads y values
    my_file = open("y.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    return new_char

def ReaderX(): #this fuction reads x values
    my_file = open("x.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    return new_char

def refresh(z): #this fuction refresh the graph
    Y = ReaderY()
    B = 'b'
    o = ReaderX()
    Tendency = Y[4] - Y[3]
    AvanzadorY(Y, Tendency, timesUp, timesFrezze, timesDown)
    x = AvanzadorX(o)
    SaveY(Y)
    SaveX(x)
    plot(Y,B)
    z = z+1


def comprar(saldo, num): #this fuction let you buy stocks
    my_file = open("y.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    saldo = saldo - new_char[9] * num
    return saldo

def vender(saldo, num): #this fuction let you sell stocks
    my_file = open("y.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    saldo = saldo + new_char[9] * num
    return saldo 

def acc(saldo, hasacc): #this fuction its the interactive part of the program
    while True:
        print("Desea comprar, vender, o pasar?")
        a = input()
        if a == "comprar":
            print("Cuantas acciones?")
            num = input()
            accionval = ReaderY()
            if(saldo >= int(num) * accionval[9]):
                saldo = comprar(saldo, int(num))
                hasacc = int(num)
                return saldo, hasacc
            else:
                print("Saldo insuficiente, pruebe con menos acciones")
        if a == "vender" and hasacc >= 1:
            saldo = vender(saldo, hasacc)
            hasacc = 0
            return saldo, hasacc
        if a == "pasar":
            return saldo, hasacc
        if a == "vender" and hasacc == 0:
            print("Usted no tiene acciones para vender")        
        else:
            print("Comando desconocido")

def ini(): #this fuction plots the firts graph
    Y = IniRandomY(0,50)
    SaveY(Y)
    SaveX(x)
    A = 'Inicial' #name of the graph
    plot(Y,A)





print("--------------------------------------------------")
print("-               Simulador de bolsa               -")
print("-               By Ignacio Joaquin               -")
print("--------------------------------------------------")
print(" ")
print(" ")
print("Tiene un saldo de $100")
saldo = 100 #inicial saldo

ini() #start the stocks
while i==0: 
    saldo, hasacc = acc(saldo, hasacc) #ask what you want to do
    print("Saldo restante " + str(saldo)) #let you now the saldo
    plt.close() #close the old graph
    refresh(z) #new graph