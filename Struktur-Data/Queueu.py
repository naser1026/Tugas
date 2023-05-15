Numbers = [1,2,3,4]
while True :
    print("\nAntrean Sekarang = ", Numbers)
    print("\n1. Tambah Nilai\n2. Hapus Nilai\n3. Keluar")
    userOption = int(input('\nPilih Opsi : '))
    if userOption == 1 :
        newNumber = int(input('\nMasukan Angka : '))
        Numbers.append(newNumber)
    elif userOption == 2 :
        buffer = []
        for i, item in enumerate (Numbers)  :
            if i == 0 :
                continue
            else :
                buffer.append(item)
        Numbers = buffer
    elif userOption == 3 :
        break
    
    
    
    
    