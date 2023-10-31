from random import randrange
import pickle

try:
    with open('b.pickle', 'rb') as file_db:
        b = pickle.load(file_db)
except (FileNotFoundError, EOFError):
    b = {}

epsedo = input("Antre non w san espas ak let majiskil : ")

print(f"Bonjou, {epsedo} ")

while ' ' in epsedo or not epsedo.islower():
    epsedo = input("Antre non w san espas ak let miniskil ladan l : ")

with open('b.pickle', 'wb') as file_db:
    pickle.dump(b, file_db)

while True:
    sekre = randrange(0, 30)
    chance = 5
    score = 0
    nouvo_s = 0

    print("Ou gen selman 5 chans ")

    
    if epsedo in b:
        print(f"Ou gen yon ansyen sko: {b[epsedo]}")

    while chance > 0:
        try:
            devine = int(input(f"Chans ou rete : {chance}. Chwazi yon nonb ant 0 ak 30 : "))

            if 0 <= devine < 30:
                if devine < sekre:
                    print("Nonb ou devine a pi piti ke nonb sekre a.")
                elif devine > sekre:
                    print("Nonb ou devine a pi gwo ke nonb sekre a.")
                else:
                    print("Bravo, ou genyen.")
                    if devine == sekre:
                        print(f"Bravo, ou genyen nonb lan ({sekre}).")
                        score = chance * 30

                        if epsedo in b:
                            a = b[epsedo]
                            b[epsedo] += score
                            print(f"Ansyen sko ou se {a}, Nouvo sko ou se {b[epsedo]}")
                        else:
                            b[epsedo] = score
                            print(f"Nouvo sko ou se {b[epsedo]}")

                        with open('b.pickle', 'wb') as file_db:
                            pickle.dump(b, file_db)
                        break
                    else:
                        print(" nonb sekre a diferan.")
                chance -= 1
            else:
                print("Nonb lan dwe ant 0 ak 30.")
                continue
        except ValueError:
            print("Ou mal devine.")

    j = input("Peze K siw vle kanpe? ")
    if j.lower() == 'k':
        chance = 0
        break
    else:
        sekre = randrange(0, 30)
        chance = 5
