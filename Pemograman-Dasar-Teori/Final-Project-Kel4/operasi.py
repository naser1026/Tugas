# import locale untuk mengubah bentuk data menjadi mata uang
import locale
locale.setlocale(locale.LC_ALL, '')

# Untuk menyimpan menu cafe bisa menggunakan dictionary 2 dimensi
# Data Makanan Berupa Dictionary dengan Kode Makanan sebagai key dan valuenya berupa dictionary yang di dalamnya ada dua key dan value yaitu nama makanan dan harga makanan
foodDict = {
    '01' : {'name' : 'Steak Ayam', 'price' : 25000},
    '02' : {'name' : 'Steak Sirloin Sapi', 'price' : 45000},
    '03' : {'name' : 'Steak Kambing', 'price' : 45000},
    '04' : {'name' : 'Nasi Gurih', 'price' : 15000},
    '05' : {'name' : 'Nasi Goreng', 'price' : 25000},
    '06' : {'name' : 'Mie Ayam', 'price' : 15000},
    '07' : {'name' : 'Dimsum Ayam', 'price' : 15000},
    '08' : {'name' : 'Dimsum Sapi', 'price' : 20000},
    '09' : {'name' : 'Dimsum Jamur', 'price' : 15000},
    '010' : {'name' : 'Keripik Ubi', 'price' : 5000},
    }

# Data Minuman Berupa Dictionary dengan Kode Minuman sebagai key dan valuenya berupa dictionary yang di dalamnya ada dua key dan value yaitu nama minuman dan harga minuman
drinkDict = {
    '01' : {'name' : 'Jus Apel', 'price' : 15000},
    '02' : {'name' : 'Jus Jeruk', 'price' : 15000},
    '03' : {'name' : 'Jus Alpukat', 'price' : 15000},
    '04' : {'name' : 'Jus Mangga', 'price' : 15000},
    '05' : {'name' : 'Cappucino', 'price' : 15000},
    '06' : {'name' : 'Air Mineral', 'price' : 10000},
    '07' : {'name' : 'Kopi Tubruk', 'price' : 10000},
}

# Data menu tambahan berupa dictionary dengan kode minuman sebagai key dan valuenya berupa dictionary yang di dalamnya ada dua key dan value yaitu nama menu tambahan dan harga menu tambahan
extraDict = {
    'A' : {'name' : 'Nasi Uduk', 'price' : 5000},
    'B' : {'name' : 'Nasi Putih', 'price' : 5000},
    'C' : {'name' : 'Kuah Soto', 'price' : 5000},
}
# Dictionary data digunakan untuk menyimpan setiap menu yang ditambahkan oleh pelanggan dengan kondisi awal kosong
dataDict = {}

# Fungsi add() digunakan untuk user agar bisa menginputkan kode dari masing-masing menu, kemudian dari inputan tersebut akan menghasilkan beberapa nilai dari variabel seperti nama dan harga dari masing - masing menu  serta harga kotor, pph, dan total tagihan
def add() :
    print("-"*141)
    # Dictionary subData untuk menyimpan data sementara
    subData = {}
    # User menginput data, nilai dari data tersebut dimasukan kedalam dictionary subData
    print("\nMasukan Data Pesanan")
    subData['name'] = input('Nama Pelanggan\t: ')
    subData['foodCode'] = str(input('Kode Makanan\t: '))
    subData['drinkCode'] = str(input('Kode Minuman\t: '))
    subData['extraCode'] = str.upper(input('Kode Menu Tambahan (isi "-" jika tidak ada) : '))
    
    # Dari inputan tersebut dengan menjadikan nilainya sebagai key untuk mengakses value dari daftar menu, maka kita dapat memasukan variabel - variabel yang dibutuhkan besarta nilainya kedalam dictionary subData
    subData['foodName'] = str(foodDict[f"0{int(subData['foodCode'])}"]['name'])
    subData['foodPrice'] = str(foodDict[f"0{int(subData['foodCode'])}"]['price'])
    subData['drinkName'] = str(drinkDict[f"0{int(subData['drinkCode'])}"]['name'])
    subData['drinkPrice'] = str(drinkDict[f"0{int(subData['drinkCode'])}"]['price'])

    # Pengkondisian jika user menginputkan '-'(strip) pada extracode(Menu tambahan)
    if '-' in subData['extraCode'] :
        subData['extraName'] = '-'
        subData['extraPrice'] = 0
    else :
        subData['extraName'] = str(extraDict[subData['extraCode']]['name'])
        subData['extraPrice'] = str(extraDict[subData['extraCode']]['price'])
    subData['subTotal'] = str(int(subData['foodPrice'])+ int(subData['drinkPrice']) + int(subData['extraPrice']))
    subData['tax'] = str(int(subData['subTotal']) * 0.11)
    subData['totalPrice'] = str(int(subData['subTotal']) + float(subData['tax']))
    # Membuat variabel key dari panjang dictionary dataDict
    key = str(len(dataDict) + 1)
    # Membuat dictionary dua dimensi baru dengan variabel key sebagai key serta  dictioanary subData sebagai valuenya
    newData = {
        key : subData
    }
    # Menambahkan dictionary newData kedalam dictionary dataDict
    dataDict.update(newData)
    
# Fungsi read digunakan untuk menampilkan masing - masing elemen dari dictionary dataDict ke konsol
def read() :
    print("-"*141)
    # Pengkondisian jika dictionary dataDict kosong
    if not dataDict :
        pesan = "Data Masih Kosong Silahkan Tambahkan Terlebih Dahulu"
        print(f"{pesan:^140}")
    else :
        # Header 
        NO = "No."
        NAME = "Nama Pelanggan"
        FOODNAME = "Nama Makanan"
        DRINKNAME = "Nama Minuman"
        EXTRANAME = "Menu Tambahan"
        TOTALPRICE = "Total Bayar"
        judul = "DAFTAR PEMBAYARAN MAKANAN"
        print(f"{judul:^141}")
        print("="*141)
        print(f"|{NO:3}|{NAME:30}|{FOODNAME:30}|{DRINKNAME:30}|{EXTRANAME:30}|{TOTALPRICE:11}|")
        print("-"*141)
    
    # Body
        # Iterasi sebanyak panjang dari dictionary data
        for i in range(len(dataDict)) :
            no = i + 1
            totalPrice = float(dataDict[f'{no}']['totalPrice'])            
            # Untuk mengubah harga dari menu menjadi format rupiah
            rpPrice = locale.currency(totalPrice,grouping=True ) [:-3]
            
            # Menampilkan data ke konsol dengan menggunakan nilai i sebagai key untuk memanggil elemen dari dictionary data
            print(f"|{f'{no}.':<3}|{dataDict[f'{no}']['name']:30}|{dataDict[f'{no}']['foodName']:30}|{dataDict[f'{no}']['drinkName']:30}|{dataDict[f'{no}']['extraName']:30}|{rpPrice:>11}|")
            
            # Pengkondisian untuk menghilangkan garis di iterasi terakhir
            if i != len(dataDict) - 1 :
                print("-"*141)
        
        # Footer
        print("="*141)
            
    
            
# Fungsi search() digunakan untuk mencari data dari dictionary dataDict dengan inputan elemen nama pelanggan
def search() :
    print("-"*141)
    # Pengkondisian jika dictionary dataDict kosong
    if not dataDict :
        pesan = "Data Masih Kosong Silahkan Tambahkan Terlebih Dahulu"
        print(f"{pesan:^140}")
    else :
        # Digunakan str.lower agar menghindari case sensitive
        userInput = str.lower(input("Masukan Nama Pelanggan : "))
        print("-"*141)
        
        # Iterasi sebanyak panjang dari dictionary dataDict ditambah 1
        for i in range(len(dataDict)) :
            # Pengkondisian jika inputan user terdapat dalam dataDict[i]['name']
            no = i + 1
            if userInput in str.lower(dataDict[f'{no}']['name']) : 
                # Jika terdapat nama pelanggan yang sesuai dengan inputan user maka dapat digunakan nilai i sebagai key untuk mengakses elemen atau value dari dictionary dataDict 
                NO = f"{no}."
                NAME = f"{dataDict[f'{no}']['name']}"
                FOODNAME = f"{dataDict[f'{no}']['foodName']}"
                DRINKNAME = f"{dataDict[f'{no}']['drinkName']}"
                PACKAGE = f"{FOODNAME} + {DRINKNAME}"
                EXTRANAME = f"{dataDict[f'{no}']['extraName']}"
                TOTALPRICE = float(dataDict[f'{no}']['totalPrice'])
                RPPRICE = locale.currency(TOTALPRICE,grouping=True ) [:-3]
                # Menampilkan hasil ke konsol
                print(f"|{NO:<3}|{NAME:30}|{PACKAGE:56}|{EXTRANAME:30}|{RPPRICE:>16}|")
                print("-"*141)