def afiche(lis):
    pi_piti = min(lis)
    pi_gran = max(lis)

    print("Pi piti nomb lan se :", pi_piti)
    print("pi gran nonb lan se:", pi_gran)


nomb = [int(nonb) for nonb in input("Antre nonb yo ak espas : ").split()]

afiche(nomb)
