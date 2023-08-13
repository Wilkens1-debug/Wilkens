from random import randrange

while True:
    n = randrange(0, 100)  
    chans = 5

    print("Men jwet male a, ou gen 5 chans")

    g = False

    while chans > 0:
        try:
            N = int(input(f"Chans ou rete : {chans}. Chwazi yon nonb ant 0 ak 100 : "))
            
            if 0 <= N <= 100:
                if N == n:
                    print(f"Ou genyen ! Ou jwen bon nonb lan ({n}).")
                    g = True
                    break
                else:
                    print("Nonb odinate a chwazi a diferan.")
            else:
                print("Cwazi yon nonb ant 0 ak 100.")
                continue  
            
            chans-= 1
        except ValueError:
            print("nonb ou a pa bon.")

    if not g:
        print(f"ou pedi Ou pa gen chans anko. nonb odinate a se : {n}")
        kontinye = input("Ou vle kontinye ? Tape 0 pou kontinye, 1 pou kanpe : ")
        if kontinye == "1":
            print("Mesi paske w te jwe avek nou !")
            break
    else:
        print("Félisitasyon ou genyen.")
        kontinye = input("Ou vle kontinye ? Tape 0 pou kontinye, 1 pou kanpe : ")
        if kontinye == "1":
            break
