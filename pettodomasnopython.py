#prva zadaca
"""
def pecati_zdravo (ime):
    print("Pozdrav ",ime)

ime = input("Vnesete ime: ")
pecati_zdravo(ime)
"""
#vtora zadaca
"""
def zbir(x,y):
    z = x + y
    if z%2==0:
        print("Zbirot na {} i {} iznesuva {} i e paren broj ".format(x,y,z))
    else:
        print("Zbirot na {} i {} iznesuva {} i e neparen broj ".format(x,y,z))

x = int(input("Vnesete broj: "))
y = int(input("Vnesete broj: "))
zbir(x,y)
"""
#treta zadaca
"""
def najgolem_broj (a,b,c):
    if a>c and a>b:
        print("Od broevite {} i {} i {}, brojot {} e najgolem broj ".format(a,b,c,a))
    elif b>c and b>a:
        print("Od broevite {} i {} i {}, brojot {} e najgolem broj ".format(a,b,c,b))
    else:
        print("Od broevite {} i {} i {}, brojot {} e najgolem broj ".format(a,b,c,c))

a = int(input("Vnesete broj: "))
b = int(input("Vnesete broj: "))
c = int(input("Vnesete broj: "))
najgolem_broj(a,b,c)
"""
#cetvrta zadaca
"""
def plostina(a,b):
    P = a * b
    print(P)
def perimetar(a,b):
    L = 2*a + 2*b
    print(L)

a=int(input("Vnesi ja dolzinata na pravoagolnikot: "))
b=int(input("Vnesi ja sirinata na pravoagolnikot: "))
prasanje = input("Dali sakate da se presmeta plostina ili perimetar na pravoagolnikot? P/L ")
if prasanje.upper()=="P":
    plostina(a,b)
else:
    perimetar(a,b)
"""
#petta zadaca

def prosek (lista):
    prosek_fin = sum(lista)/len(lista)
    print("Prosekot na elementite vo listata e: ",prosek_fin)
lista = []
while True:
    x = int(input("Vnesi element od 1 do 5 vo listata: "))
    lista.append(x)
    answer = input("Dali sakate da vnesete uste elementi? da/ne ")
    if answer.lower() == "da":
        pass
    else:
        break
prosek(lista)
