# Mengimport modul operasi (Tanda '*' memiliki arti bahwa semua fungsi didalam modul dapat diakses)
from operasi import *
import os

while True :
    # os.system('cls') digunakan untuk membersihkan konsol
    os.system("cls")    
    print("="*141)
    TITLE = "PROGRAM MANAJEMEN TRANSAKSI CAFE ABCD"
    print(f"{TITLE:^141}")
    print("="*141)
    print("\n1. Tambah Pembayaran")
    print("2. Daftar Pembayaran Makanan")
    print("3. Cari Pesanan")
    userOption = int(input("\nPilih Opsi\t: "))
    match userOption :
        # Panggil fungsi dari modul operasi sesuai case yang diinputkan user
        case 1 : add()
        case 2 : read()
        case 3 : search()
    
    # Pengkondisian jika user selesai 
    stop = str.lower(input("\nApakah Selesai (y/n)? "))
    if stop == 'y' :
        break

os.system("cls")
print("+++++++++++++PROGRAM SELESAI+++++++++++++")