a = int(input("Antre premye nonb a : "))
b = int(input("Antre dezyèm nonb b : "))
x = int(input("Antre valè a pou enteval la : "))
y = int(input("Antre valè b pou enteval la : "))

def miltip(a, b, n):
    return n % a == 0 and n % b != 0

def miltip_a_san_b(a, b, n):
    return n % b == 0 and n % a != 0

def miltip_b_san_a(a, b, n):
    return n % a == 0 and n % b == 0

def ni_a_ni_b(a, b, n):
    return n % a != 0 and n % b != 0

total_miltip_a_pas_b = 0
total_miltip_b_pas_a = 0
total_miltip_a_ak_b = 0
total_pa_miltip = 0

for n in range(x, y + 1):
    if miltip(a, b, n):
        print(f"{n} se yon miltip {a} men pa {b}")
        total_miltip_a_pas_b += 1
    if miltip_a_san_b(a, b, n):
        print(f"{n} se yon miltip {b} men pa {a}")
        total_miltip_b_pas_a += 1
    if miltip_b_san_a(a, b, n):
        print(f"{n} se yon miltip {a} ak {b}")
        total_miltip_a_ak_b += 1
    if ni_a_ni_b(a, b, n):
        print(f"{n} pa miltip ni {a} ni {b}")
        total_pa_miltip += 1

print(f"Total miltip {a} men pa {b}: {total_miltip_a_pas_b}")
print(f"Total miltip {b} men pa {a}: {total_miltip_b_pas_a}")
print(f"Total miltip {a} ak {b}: {total_miltip_a_ak_b}")
print(f"Total pa miltip ni {a} ni {b}: {total_pa_miltip}")
