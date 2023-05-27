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
    print("6. Selesai")
    while True :
        try :
            userOption = int(input("\nPilih Opsi\t: "))
            if userOption <=6 and userOption > 0 :
                break
            else :
                print("Opsi tidak ada")
        except :
            print("Pilihan harus angka(1...5)")
    match userOption :
        case 1 : myCafe.add() 
        case 2 : 
            if myCafe.read() == False :
                print("Database Masih Kosong, Silahkan Tambahkan Data Terlebih Dahulu")
                os.system('pause')
        case 3 : 
            if myCafe.search() == False :
                print("Database Masih Kosong, Silahkan Tambahkan Data Terlebih Dahulu")
                os.system('pause')
        case 4 : 
            if myCafe.update() == False :
                print("Database Masih Kosong, Silahkan Tambahkan Data Terlebih Dahulu")
                os.system('pause')
        case 5 : 
            if myCafe.delete() == False :
                print("Database Masih Kosong, Silahkan Tambahkan Data Terlebih Dahulu")
                os.system('pause')
        case 6 : break

clear()
print("++++++++++PROGRAM SELESAI, TERIMA KASIH++++++++++")
        
    