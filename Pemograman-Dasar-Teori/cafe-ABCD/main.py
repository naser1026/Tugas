import myCafe
import os

def clear() :
    if os.name == 'nt' :
        return(os.system('cls'))
    else :
        return(os.system('clear'))
while True :
    clear()
    print("=====================================")
    print("PROGRAM MANAJEMEN TRANSAKSI CAFE ABCD")
    print("=====================================")
    print("1. Tambah Pembayaran")
    print("2. Daftar Pembayaran Makanan")
    print("3. Cari Pesanan")
    print("4. Ubah Pesanan")
    print("5. Hapus Pesanan")
    while True :
        try :
            userOption = int(input("\nPilih Opsi\t: "))
            if userOption <=5 and userOption > 0 :
                break
            else :
                print("Opsi tidak ada")
        except :
            print("Pilihan harus angka(1...5)")
    match userOption :
        case 1 : myCafe.add()
        case 2 : myCafe.read()
        case 3 : myCafe.search()
        case 4 : myCafe.update()
        case 5 : myCafe.delete()
    
    stop = str.lower(input("\nApakah Selesai (y/n)? "))
    if stop == 'y' :
        break
clear()
print("++++++++++PROGRAM SELESAI, TERIMA KASIH++++++++++")
        
    