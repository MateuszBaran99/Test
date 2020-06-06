import random
import os

def rozdanie():
    os.system('cls')
    #uwagi i zasady
    print("UWAGA! JEZELI WPISZESZ COS INNEGO POZA LICZBAMI Z INSTRUKCJI... PROGRAM SIE WYSYPIE!")
    reka = []
    gracze = []
    n = int(24/4)
    karty = ["AsP","9P", "10P", "jopekP", "damaP", "krolP", 
    "AsK", "9K", "10K", "jopekK", "damaK", "krolK", 
    "AsT", "9T", "10T", "jopekT", "damaT", "krolT", 
    "AsKa", "9Ka", "10Ka", "jopekKa", "damaKa", "krolKa"]
    for j in range(4): #tasowanie kart dla graczy
        for i in range(n):
            wybor_karty = random.randint(0, len(karty)-1)
            karta = karty[wybor_karty]
            karty.pop(wybor_karty)
            reka.append(karta)
        gracze.append(reka)
        reka = []
    
    for q in range(len(gracze)): #ustala ktory gracz zaczyna
        for p in range(len(gracze[1])):
            if gracze[q][p] == "9K":
                Pgracz = q
    stos = []
    while (len(gracze[0]) != 0) or (len(gracze[1]) != 0) or (len(gracze[2]) != 0) or (len(gracze[3]) != 0):
        #print("\n", gracze)
        print(f"Gracz numer {Pgracz +1}\n") 
        stoper = input("Gotowy? Kliknij ENTER...")
        print(gracze[Pgracz])
        ruch = input("wurzut = index, dobierz = 8, dobierz 3 karty = 9, wyrzuc 3 karty = 7, wyrzuc 4 karty = 6:  ")
        ruch = int(ruch)
        #if ruch == 9:  #pomin opcja
            #if Pgracz < 3:
                #Pgracz = Pgracz + 1
            #else:
                #Pgracz = Pgracz - 3
        if ruch == 8: #dobierz
            gracze[Pgracz].append(stos[len(stos)-1])
            stos.pop(len(stos)-1)
            if Pgracz < 3:
                Pgracz = Pgracz + 1
            else:
                Pgracz = Pgracz - 3
        elif ruch == 9: #dobierz 3 karty
            gracze[Pgracz].append(stos[len(stos)-1])
            stos.pop(len(stos)-1)
            gracze[Pgracz].append(stos[len(stos)-1])
            stos.pop(len(stos)-1)
            gracze[Pgracz].append(stos[len(stos)-1])
            stos.pop(len(stos)-1)
            if Pgracz < 3:
                Pgracz = Pgracz + 1
            else:
                Pgracz = Pgracz - 3
        elif ruch == 7: #wyrzuc 3 karty
            ruch3 = input("wybierz pierwsza")
            ruch3 = int(ruch3)
            stos.append(gracze[Pgracz][ruch3])
            gracze[Pgracz].pop(ruch3)
            print(gracze[Pgracz])
            ruch3 = input("wybierz druga")
            ruch3 = int(ruch3)
            stos.append(gracze[Pgracz][ruch3])
            gracze[Pgracz].pop(ruch3)
            print(gracze[Pgracz])
            ruch3 = input("wybierz trzecia")
            ruch3 = int(ruch3)
            stos.append(gracze[Pgracz][ruch3])
            gracze[Pgracz].pop(ruch3)

            if Pgracz < 3:
                Pgracz = Pgracz + 1
            else:
                Pgracz = Pgracz - 3
        elif ruch == 6: #wyrzuc 4 karty
            ruch4 = input("wybierz pierwsza")
            ruch4 = int(ruch4)
            stos.append(gracze[Pgracz][ruch4])
            gracze[Pgracz].pop(ruch4)
            print(gracze[Pgracz])
            ruch4 = input("wybierz druga")
            ruch4 = int(ruch4)
            stos.append(gracze[Pgracz][ruch4])
            gracze[Pgracz].pop(ruch4)
            print(gracze[Pgracz])
            ruch4 = input("wybierz trzecia")
            ruch4 = int(ruch4)
            stos.append(gracze[Pgracz][ruch4])
            gracze[Pgracz].pop(ruch4)
            ruch4 = input("wybierz czwarta")
            ruch4 = int(ruch4)
            stos.append(gracze[Pgracz][ruch4])
            gracze[Pgracz].pop(ruch4)

            if Pgracz < 3:
                Pgracz = Pgracz + 1
            else:
                Pgracz = Pgracz - 3

        else: #wyrzuc
            stos.append(gracze[Pgracz][ruch])
            gracze[Pgracz].pop(ruch)
            if Pgracz < 3:
                Pgracz = Pgracz + 1
            else:
                Pgracz = Pgracz - 3
        #jezeli karta to trefl to cola kolejke do poprzedniego gracza
        if stos[len(stos) - 1] == "AsT" or stos[len(stos) - 1] == "9T" or stos[len(stos) - 1] == "10T" or stos[len(stos) - 1] == "jopekT" or stos[len(stos) - 1] == "damaT" or stos[len(stos) - 1] == "krolT":
            if Pgracz == 0:
                Pgracz = Pgracz + 2
            elif Pgracz == 1:
                Pgracz = Pgracz + 2
            else:
                Pgracz = Pgracz - 2
                
        os.system('cls') #czysci konsole
        print("stos: \n", stos)
        #wygrana
        if (len(gracze[0]) == 0) or (len(gracze[1]) == 0) or (len(gracze[2]) == 0) or (len(gracze[3]) == 0):
            #poprawka na to jezeli ostatnia karta w stosie to trefl
            if stos[len(stos) - 1] == "AsT" or stos[len(stos) - 1] == "9T" or stos[len(stos) - 1] == "10T" or stos[len(stos) - 1] == "jopekT" or stos[len(stos) - 1] == "damaT" or stos[len(stos) - 1] == "krolT":
                if Pgracz == 2 or Pgracz == 3:
                    Pgracz = Pgracz - 2
                else:
                    Pgracz = Pgracz + 2
            if Pgracz == 0:
                print("wygrał gracz: 4")
                return 0
            print("wygral gracz: ", Pgracz)
            return 0

rozdanie()