from os import timesSubiendo
import random

def LectorY():
    my_file = open("y.txt", "r")
    data = my_file.read()
    data_into_list = data.split(" ")
    new_char = [int(x) for x in data_into_list]
    return new_char

def GuardarY(Y):
    Ystr = ' '.join(map(str, Y))
    with open('y.txt', 'w') as f:
        f.write(Ystr)

Yvieja = LectorY()
Tendencia = Yvieja[4]-Yvieja[3]
def Decididor(Tendencia):
    if Tendencia > 0: #si aumenta
        chances = random.randint(0,100)
        if timesSubiendo == 0:
            if chances < 41 :
                return 1
                timesSubiendo = timesSubiendo+1
        
            if chances >= 41 and chances <= 70:
                return 0
        
            if chances > 70 :
                return -1
        
        if timesSubiendo == 1:
            if chances < 31 :
                return 1
        
            if chances >= 31 and chances <= 70 :
                return 0
        
            if chances > 70 :
                return -1 

        if timesSubiendo > 1:
            if chances < 21 :
                return 1
        
            if chances >= 21 and chances <= 60 :
                return 0
        
            if chances > 60 :
                return -1                       

    if Tendencia == 0: #si viene igual


