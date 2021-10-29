import math
def prviZadatak():
    nugao = int(input())
    nugaomin = int(input())
    nugaosec = int(input())
    ukupnoSec = nugao*60*60 + nugaomin*60 + nugaosec
    prav = 90*60*60
    if ukupnoSec < prav:
        print(ukupnoSec, "ostar")
    if ukupnoSec == prav:
        print(ukupnoSec, "prav")
    if ukupnoSec > prav:
        print(ukupnoSec, "tup")

def drugiZadatak():
    ucenici = int(input())
    dramci = int(input())
    kosarka = int(input())
    oba = (kosarka+dramci)-ucenici
    print(oba)
    if oba>=5 and dramci >= 10 and kosarka >=10:
        print("super")

def treciZadatak():
    a = int(input())
    b = int(input())
    c = int(input())

    brojevi = [a,b,c]
    brojevi.sort()
    
    baka = brojevi[2]
    cerka = brojevi[0]
    tata = brojevi[1]
    print(baka,cerka,tata)
    #NIJE ZAVRSENO.
    #FINISHME
    

#prviZadatak()
#drugiZadatak()   
treciZadatak()
