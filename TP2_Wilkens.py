from random import choice, randint

def Inisyal(non):
    ini = "".join(part[0] for part in non.split())
    return ini.upper()

def epsedo(Non, Siyati):
    Non = Non.capitalize()
    Siyati = Siyati.lower()

    ini = Inisyal(Non) + Inisyal(Siyati)
    epsedo1 = f"{ini}16"
    
    a = Non.split()
    b = Siyati.split()
    tout_non = "".join(a + b)
    epsedo2 = tout_non
    
    ti_non = min(Non, Siyati, key=len)
    random_nonb = randint(100, 1000)
    
    Non_pi_kout = ti_non[::-1]
    premye_let = Non_pi_kout[0].upper()
    res_yo = Non_pi_kout[1:].lower()
    epsedo3 = f"{premye_let}{res_yo}{random_nonb}"

    print(f"Epsedo 1: {epsedo1}")
    print(f"Epsedo 2: {epsedo2}")
    print(f"Epsedo 3: {epsedo3}")

    return [epsedo1, epsedo2, epsedo3]

def main():
    Non = input("Antre non w : ")
    Siyati = input("Antre Siyati w : ")

    epse = epsedo(Non, Siyati)
    lis = epse

    with open("database.txt", "r") as fichye:
        w = fichye.read().strip()
        epsedo_lis = w.split(",")

    kantite = len(epsedo_lis)

    print(f"Bonjou {Non} {Siyati}, nou rekoni nan sevis sa a.")
    print(f"Nou deja jenere epsedo pou {kantite} moun deja.")

    chwa = choice(lis)
    epsedo_lis.append(chwa)

    with open("database.txt", "w") as fichye:
        epsedo_lis[kantite] = chwa
        fichye.write(",".join(epsedo_lis))

    print("Non ki sanble favorab pou itilize a se :", chwa)

if __name__ == "__main__":
    main()
