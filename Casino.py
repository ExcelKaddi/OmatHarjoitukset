import random
import time
omat = []
jakaja = []
wallet = 100
panos = 0
def error():
    print("Error, Yritä uusiksi")

#Wallet
def walletmuutto():
    global wallet
    global panos
    wallet -= panos
def walletvoitto():
    global wallet
    global panos
    wallet += panos
#BlackJack H/S
def jakajannosto():
    print("Jäit ja numerosi on", omat[0])
    while True:
        number = random.randint(2,11)
        if jakaja[0] <= omat[0]:
            print("Jakaja nostaa...")
            jakaja[0] += number
            time.sleep(0.2)
            print("Jakajan kortit on", jakaja[0])
        if jakaja[0] > omat[0] and jakaja[0] < 21:
            print("Jakaja voitti.")
            walletmuutto()
            menu()
        if jakaja[0] > 21:
            print("Jakaja bustasi, voitit")
            walletvoitto()
            menu()
        if jakaja[0] == 21:
            print("Jakaja sai blackjakin")
            print("Jakaja voitti")
            walletmuutto()
            menu()
def hittaus():
    while True:
        number = random.randint(2,11)
        omat[0] += number
        print("Nostit ja numerosi on", omat[0])
        if omat[0] > 21:
            print("Bustasit ja hävisit")
            walletmuutto()
            menu()
        if omat[0] == 21:
            print("Sait blackjackin")
            break
        if omat[0] < 21:
            break
#Games
def blackjack():
    bet = int(input("Panos: "))

    x = random.randint(2,11)
    x2 = random.randint(2,10)
    omat.append(x2 + x)
    print("Ekat numerosi on ", x+x2)
    x3 = random.randint(2,11)
    x4 = random.randint(2,10)
    jakaja.append(x3 + x4)
    print("Jakajan ekat numerot on", x3 + x4)
    while True:
        global panos
        global wallet
        panos += bet
        if panos > wallet:
            error()
        else:
            break
    while True:
        print("H OR S")
        hit = input("")
        if hit == "S":
            jakajannosto()
        if hit == "H":
            hittaus()  
def coinflip():
    x = random.randint(1,2)
    global panos
    global wallet
    bet = int(input("Panos:"))
    while True:
        global panos
        global wallet
        panos += bet
        if panos > wallet:
            error()
        else:
            break
    input("Valitse väri P/M: ")
    print("Kolikkoa heitetään...")
    time.sleep(0.2)
    if x==1:
        print("Voitit betin")
        walletvoitto()
        menu()
    if x==2:
        print("Hävisit betin")
        walletmuutto()
        menu()
def lotto(amount,limit):
    lista = []
    lista2 = []
    oikeinmenneet = []
    for i in range(amount):
        satuinnaisluku = random.randint(1,limit)
        while True:
            if satuinnaisluku in lista:
                satuinnaisluku = random.randint(1,limit)
            if satuinnaisluku not in lista:
                lista.append(satuinnaisluku)
                break
    for i in range(amount):
        while True:
            try:
                print("Arvaa lottonumero [",i+1,"/",len(lista),"]")
                e1 = int(input(""))
                if e1>limit:
                    error()
                else:
                    lista2.append(e1)
                    break
            except ValueError:
                error()
    for i in range(amount):
        if lista[i] in lista2:
            oikeinmenneet.append(lista[i])
    if len(oikeinmenneet)==amount:
        print("Voitit numeroilla",lista2)
        menu()
    if len(oikeinmenneet)<amount:
        print("Sait",len(oikeinmenneet),"oikein")
        print("Oikeat voittonumerot olivat",lista2)
        menu()
    if len(oikeinmenneet)<=4:
        menu()
    if len(oikeinmenneet)<=3:
        menu()
#Menu
def menu():
    while True:
        while True:
            if wallet>=1000:
                print("Sinulla on yli tonni rahaa..")
                print("Voitit pelin!")
                exit()
            if wallet==0:
                print("Sinulla ei ole enään rahaa..")
                print("Hävisit pelin")
                exit()
            if wallet>0:
                break
        print("Wallet Balance", wallet)
        print("[1] Coinflip [2] Blackjack [3] Lotto")
        valitse = int(input(""))
        if valitse==2:
            blackjack()
        if valitse==1:
            coinflip()
        if valitse==3:
            lotto(7,41)

menu()
