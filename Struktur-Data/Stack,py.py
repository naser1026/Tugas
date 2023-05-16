listBuku = ["Matematika", "Biologi", "Kimia"]
print("Kondisi Tumpukan Sekarang : ", listBuku)
while True : 
    print("\n1. Tambah Buku\n2. Hapus Buku")
    userOption = int(input('Pilih Opsi : '))
    if userOption == 1 :
        newBook = input("\nMasukan Judul Buku : ")
        listBuku.append(newBook)
    else :
        listBuku.pop()
    print("\nKondisi Tumpukan Sekarang : ", listBuku)
    isDone = str.lower(input("\nApakah Selesai (y/n)? "))
    if isDone == 'y' :
        break
    



    
    
    
    

