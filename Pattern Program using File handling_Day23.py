#RAT - NUM - ROW

def RAT():
    f=open('Pattern Program.txt', 'w+')
    f.write('========================\n')
    f.write('ROW RIGHT ANGLE TRIANGLE\n')
    f.write('==========================')
    for i in range(0,9):
        for j in range(i):
            f.write(str(i))
        f.write('\n')
    f.close()

    
RAT()

#CRAT - NUM - ROW
def CRAT():
    f=open('Pattern Program.txt', 'a+')
    f.write('============================\n')
    f.write('COLUMN RIGHT ANGLE TRIANGLE\n')
    f.write('============================')
    for i in range(0,9):
        for j in range(i):
            f.write(str(j))
        f.write('\n')
    f.close()

    
CRAT()

#INVERSE STAR RIGHT ANGLE TRIANGLE:
def ISRAT():
    f= open('Pattern Program.txt', 'a+')
    f.write('====================================\n')
    f.write('INVERSE STAR RIGHT ANGLE TRIANGLE\n')
    f.write('====================================\n')
    for i in range(9,0,-1):
        for j in range(i):
            f.write('*')
        f.write('\n')
    f.close()

    
ISRAT()

#RAT - UPPER - ROW
def ARAT():
    f= open('Pattern Program.txt', 'a+')
    f.write('====================================\n')
    f.write('ALPHABET RIGHT ANGLE TRIANGLE\n')
    f.write('====================================\n')
    for i in range(0,15):
        for j in range(i):
            f.write(chr(i+64))
        f.write('\n')
    f.close()

ARAT()


#RAT - NAME - ROW
NAME = 'VAN VICTOR DOOM'
def NRAT():
    f= open('Pattern Program.txt', 'a+')
    f.write('====================================\n')
    f.write('NAME RIGHT ANGLE TRIANGLE\n')
    f.write('====================================\n')
    for i in range(len(NAME)):
        for j in range(i+1):
            f.write(NAME[i])
        f.write('\n')
    f.close()

NRAT()






#HEART 

'''HK = [(1,5),(1,6),(1,7),(1,8),(1,12),(1,13),(1,14),(1,15),(2,3),(2,4),(2,9),(2,11),(2,16),(2,17),(3,2),(3,10),
         (3,18),(4,1),(4,19),(5,1),(5,19),(6,1),(6,19),(7,1),(7,19),(8,2),(8,18),(9,3),(9,17),(10,4),(10,16),(11,5),(11,15),
         (12,6),(12,14),(13,7),(13,13),(14,8),(14,12),(15,9),(15,11),(16,10)]

def HT():
    for i in range(1,20):
        for j in range(1,30):
            if (i,j)in HK:
                print('*', end = ' ' )
            else:
                print('.', end = ' ' )
        print()


HT()'''





'''#HEART WITH ARROW:
Heart = [(1,5),(1,6),(1,7),(1,8),(1,12),(1,13),(1,14),(1,15),(2,3),(2,4),(2,9),(2,11),(2,16),(2,17),(3,2),(3,10),
         (3,18),(4,1),(4,19),(5,1),(5,19),(6,1),(6,19),(7,1),(7,19),(8,2),(8,18),(9,3),(9,17),(10,4),(10,16),(11,5),(11,15),
         (12,6),(12,14),(13,7),(13,13),(14,8),(14,12),(15,9),(15,11),(16,10),
         (13,0),(12,2),(11,4),(10,6),(9,8),(8,10),(7,12),(6,14),(5,16),(4,18),(3,20),(2,22),(1,24),(1,24),
         (2,24),(2,23),(1,23),(13,0),(12,0),(14,0),(13,1),(12,1)]

def AHRT():
    for i in range(1,20):
        for j in range(1,30):
            if (i,j)in Heart:
                print('*', end = ' ' )
            else:
                print('.', end = ' ' )
        print()


AHRT()'''










    
    
    
    


