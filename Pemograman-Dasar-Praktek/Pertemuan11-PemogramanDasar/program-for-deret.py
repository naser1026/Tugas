print("===========================")
print(" PROGRAM DERET ARITMATIKA ")
print("===========================")

suku = int(input("Masukan Suku Awal\t: "))
beda = int(input("Masukan Beda\t\t: "))
banyak = int(input("Masukan Banyak Deret\t: "))

for i in range(1,(banyak+1)) :
    print(f"Suku ke-{i} = {suku}")
    suku += beda
