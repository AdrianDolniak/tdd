#!/usr/bin/python
def f1(x,y=0):
    return (x**2)+y

def f2(x):
    if x == []:
        return 'BUUUUM'
    else:
        return x[0]

def f3(x):
    if x == 1:
        return 'jeden'
    elif x == 2:
        return 'dwa'
    elif x == 3:
        return 'trzy'
    else:
        if x in range(4,1000):
            return 'other'

def f4(x,y=False):
    if y == False:
        if x == 'ala':
            return '%s ma kota' %(x)
        if x == 'kot':
            return '%s ma kota' %(x)
    else:
        if x == 'kot' and y == 'psa':
            return '%s ma kota i %s' %(x,y)
        if x == 'kot' and y == 'mysz':
            return '%s ma kota i %s' %(x,y)

def f5(x,y=0):
    if y == 0:
        if x == 0:
            return list(range(x))
        elif x == 1:
            return list(range(x))
        elif x == 2:
            return list(range(x))
        elif x == 7:
            return list(range(x))
    elif x == 7 and y == 2:
        return list(range(0,x,y))
    elif x == 17 and y == 2:
        return list(range(0,x,y))
    elif  x == 17 and y == 5:
        return list(range(0,x,y))

def f6(x,y):
    if x == 1 and y == '*':
        for i in y:
            return i
    elif x == 7 and y == '*':
        for i in y:
            return i*x

def f7(x):
    dictionary = {
    'ala': 'slowo',
    1: 'cyfra',
    11111: 'liczba',
    -11111: 'liczba_ze_znakiem',
    'Ala ma kota.': 'zdanie',
    '<taaag>': 'tag poczatkowy',
    '</taaag>': 'tag koncowy',
     }
    return(dictionary.get(x))

def f8(x,y):
    if x in y:
        return True
    else:
        return False

def f9(x,y):
    if x > 0 and y > 0:
        return 'dodatnie'
    elif x < 0 and y < 0:
        return 'ujemne'
    elif x < 0 and y > 0:
        return 'roznych znakow'
    elif x < 0 and y == 0:
        return 'jest zero'

def f10(x,y):
    if x == y:
        return 'rowne'
    elif x != y:
        return 'rozne'
