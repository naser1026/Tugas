print("Program Menu Menghitum Luas Bidang Sederhana")
print("============================================")

print("1. Menghitung Luas Persegi Panjang")
print("2. Menghitung Luas Lingkaran")
print("3. Menghitung Luas Segitiga")

while 1 :
    pilih = int(input('Masukan Pulihan (1,2,3) : '))
    match pilih :
        case 1 :
            print("Menghitung Luas Persegi Panjang \n")
            P = input("Panjang : ")
            L = input("Lebar : ")
            luas = float(P) * float(L)
            print("Luas : ", luas)
        
        case 2 :
            print("Menghitung Luas Lingkaran\n")
            R = input("Jari-jari : ")
            luas = 3.14*float(R)*float(R)
            print("Luas : ", luas)
        
        case 3 :
            print("Menghitung Luas Segitiga")
            A = input("Alas : ")
            T = input("Tinggi : ")
            luas = float(A)*float(T)*0.5
            print("Luas : ", luas)
        
        case _ : 
            print("Anda Memasukan Angka Yang Salah")
            
                