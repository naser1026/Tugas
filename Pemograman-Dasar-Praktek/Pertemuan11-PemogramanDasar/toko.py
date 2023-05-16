import os
totalBayar = 0
while True :
    os.system("cls")
    print("=======================================")
    print("-----------Toko Baju Unikloh-----------")
    print("---------------------------------------")
    print("\nBerikut Daftar Baju Yang Tersedia")
    print(f'{"No.":^3}|{"Nama Baju":30}|{"Harga":^15}|{"Diskon":^10}|')
    print(f'{"1":^3}|{"Seragam Pemuda Pancasila":30}|{"Rp. 150.000":^15}|{"30%":^10}|')
    print(f'{"2":^3}|{"Seragam Banser":30}|{"Rp. 200.000":^15}|{"40%":^10}|')
    print(f'{"3":^3}|{"Seragam Sunda Empire":30}|{"Rp. 175.000":^15}|{"25%":^10}|')
    
    userOption = input("\nMasukan Pilihan : ")
    if userOption == '1' :
        name = "Seragam Pemuda Pancasila"
        harga = 150000
        diskon = 0.30*harga
    elif userOption == '2' :
        name = "Seragam Banser"
        harga = 200000
        diskon = 0.40*harga
    elif userOption == '3' :
        name = "Seragam Pemuda Pancasila"
        harga = 175000
        diskon = 0.25*harga
    else :
        print("Nomor yang anda pilih tidak tersedia")

    bayar = harga - diskon
    totalBayar += bayar
    tanya = str.lower(input("Tambah Pesanan (y/n)? "))
    if tanya == 'n' :
        break
print("Total Pembayaran Anda : Rp.", totalBayar)
print("Terima Kasih Atas Kunjungannya Ke Toko UNIKLOH")
