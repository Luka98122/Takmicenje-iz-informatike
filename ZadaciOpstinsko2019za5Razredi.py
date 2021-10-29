# Opstinsko 2019

def prviZadatak():
    #print("Hi")
    n50 = int(input())
    n20 = n50*2
    n = int(input())
    print((n50*50)+(n20*20)-n*15)
    
def drugiZadatak():
    n = int(input())
    print(n*5+1)

def treciZadatak():
    ugao = int(input())
    ugaoMin = int(input())
    if ugao == 90 and ugaoMin == 0:
        print(ugao, "prav")
    if ugao>=90 and ugaoMin != 0:
        print(ugao, "tup")
    if ugao<90:
        print(ugao, "ostar")
    

if __name__=="__main__":
    #prviZadatak()
    #drugiZadatak()
    treciZadatak()
