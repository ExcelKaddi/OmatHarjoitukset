import random
import time

possible = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
def roulette():
    x = random.choice(possible)
    print("3.. 2.. 1..")
    time.sleep(0.2)
    if x==0:
        voitto = "vihreä"
        print("VIHREÄ")
    if x%2:
        voitto = "musta"
        print("MUSTA")
    else:
        if x!=0:
            voitto = "punainen"
            print("PUNAINEN")    
    if ask=="C":
        if voitto == "vihreä" and kysy=="V":
            print("VOITIT")
        if voitto == "punainen" and kysy=="P":
            print("VOITIT")
        if voitto == "musta" and kysy=="M":
            print("VOITIT")
    if ask=="N" and x in arvatut:
        print("VOITIT NUMEROLLA ", x)
    print("Numero oli ", x)



laskuri = 0
arvatut = []
while True:
    ask = input("Mille bettaat N OR C: ")
    if ask=="C":
        kysy = input("P/V/M: ")
        roulette()
    if ask=="N":
        amount = int(input("Kuinka monelle bettaat?: "))
        for i in range(amount):
            numero = int(input("NUMBER max 36: "))
            if numero > 36 or numero<0:
                if numero<0:
                    print("Liian pieni numero!")
                else:
                    print("Liian iso numero!")
            else:
                arvatut.append(numero)
                laskuri += 1
                if laskuri>=amount:
                    roulette()
