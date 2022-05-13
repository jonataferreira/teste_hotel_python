from datetime import datetime
from pickletools import int4


codL = 3
codB = 4
codR = 5
condition = 's'

while condition == 's':
    L = 0
    B = 0
    R = 0
    tipo = str(input ('Digite o tipo de cliente (Regular ou Reward): '))
    data1 = str(input ('Digite a primeira data: '))
    if ('sun' in data1 or'sat' in data1):
            if (tipo == 'Regular'):
                L += 90 
                B += 60 
                R += 150 
            else:
                L +=  80 
                B +=  50 
                R +=  40 

    else:
            if (tipo == 'Regular'):
                L += 110 
                B += 160 
                R += 220 
            else:
                L += 80 
                B += 110 
                R += 100
    print(L,B,R)


    data2 = str(input ('Digite a segunda data: '))
    if ('sun' in data2 or 'sat' in data2):
            if (tipo == 'Regular'):
                L += 90 
                B += 60 
                R += 150 
            else:
                L +=  80 
                B +=  50 
                R +=  40 

    else:
            if (tipo == 'Regular'):
                L += 110 
                B += 160 
                R += 220 
            else:
                L += 80 
                B += 110 
                R += 100
    print(L,B,R)


    data3 = str(input ('Digite a terceira: '))
    if ('sun' in data3 or 'sat' in data3 ):
            if (tipo == 'Regular'):
                L += 90 
                B += 60 
                R += 150 
            else:
                L +=  80 
                B +=  50 
                R +=  40 

    else:
            if (tipo == 'Regular'):
                L += 110 
                B += 160 
                R += 220 
            else:
                L += 80 
                B += 110 
                R += 100
    print(L,B,R)
    

  
    if ((L < B) and (L < R)):
        print('Lakewood')
    else:
        if ((B <= L) and (B < R)):
            print('Bridgewood')
        else:
            if (R <= B) and (R <= L):
                print('Ridgewood')
            else:
                print('Ridgewood')

    condition = str(input ('se quiser fazer outra consulta digite S: '))



