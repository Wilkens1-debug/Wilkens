def main():
    while True:
        try:
            n = int(input("Antre kantite not ou vle a : "))
            
            notes = []
            
            i = 0 
            
            while i < n:
                not_yo = float(input(f"Antre not  {i + 1} : "))
                notes.append(not_yo)  # Ajoute not yo non lis la
                i += 1
            print(f"Lis la se : {notes}")
            mwayen = sum(notes) / n  
            
            if mwayen >= 90:
                klasifikasyon = "A"
                print(f"Felisitasyon")
            elif mwayen >= 80:
                klasifikasyon = "B"
            elif mwayen >= 70:
                klasifikasyon = "C"
            elif mwayen >= 60:
                klasifikasyon = "D"
            else:
                klasifikasyon = "F"
            
            print(f"Mwayen ou se : {mwayen:.2f}")
            print(f"Klasifikasyon : {klasifikasyon}")
        
        except ValueError:
            print("Ou sipoze antre nonb selman.")
        
        c = input("Ou vle kontinye ? (w/n) : ")
        if c != "w":
            break

if __name__ == "__main__":
    main()
