import locale
import os

locale.setlocale(locale.LC_ALL, '')
TEMPLATE = {
    'name' : ' '*100,
    'foodCode' : '00',
    'foodName' : ' '*30,
    'foodPrice' : ' '*10,
    'drinkCode' : '00',
    'drinkName' : ' '*30,
    'drinkPrice' : ' '*10,
    'extraCode' : '00',
    'extraName' : ' '*30,
    'extraPrice' : ' '*10,
    'subTotal' : ' '*10,
    'tax' : ' '*10,
    'totalPrice' : ' '*10
}
DBNAME = 'data.txt'
food = {
    '01' : {'name' : 'Steak Ayam', 'price' : 25000},
    '02' : {'name' : 'Steak Sirloin Sapi', 'price' : 45000},
    '03' : {'name' : 'Steak Kambing', 'price' : 45000},
    '04' : {'name' : 'Nasi Gurih', 'price' : 15000},
    '05' : {'name' : 'Nasi Goreng', 'price' : 25000},
    '06' : {'name' : 'Mie Ayam', 'price' : 15000},
    '07' : {'name' : 'Dimsum Ayam', 'price' : 15000},
    '08' : {'name' : 'Dimsum Sapi', 'price' : 20000},
    '09' : {'name' : 'Dimsum Jamur', 'price' : 15000},
    '10' : {'name' : 'Keripik Ubi', 'price' : 5000},
    }
drink = {
    '01' : {'name' : 'Jus Apel', 'price' : 15000},
    '02' : {'name' : 'Jus Jeruk', 'price' : 15000},
    '03' : {'name' : 'Jus Alpukat', 'price' : 15000},
    '04' : {'name' : 'Jus Mangga', 'price' : 15000},
    '05' : {'name' : 'Cappucino', 'price' : 15000},
    '06' : {'name' : 'Air Mineral', 'price' : 10000},
    '07' : {'name' : 'Kopi Tubruk', 'price' : 10000},
}
extra = {
    'A' : {'name' : 'Nasi Uduk', 'price' : 5000},
    'B' : {'name' : 'Nasi Putih', 'price' : 5000},
    'C' : {'name' : 'Kuah Soto', 'price' : 5000},
}

def add() :
    print("\nMasukan Data Pesanan")
    name = input('Nama Pelanggan\t\t\t: ')
    while True :
        try :
            foodCode = int(input('Kode Makanan\t\t\t: '))
            if foodCode <= len(food) and foodCode > 0 :
                break
            else :
                print('Data Makanan Tidak Ditemukan')
        except :
            print(f"Pilihan Harus Angka 01 - 0{len(food)} ")
    while True :
        try :
            drinkCode = int(input('Kode Minuman\t\t\t: '))
            if drinkCode <= len(drink) and drinkCode > 0 :
                break
            else :
                print('Data Makanan Tidak Ditemukan')
        except :
            print(f"Pilihan Harus Angka 01 - 0{len(drink)} ")
    while True :
        try :
            extraCode = str.upper(input('Kode Menu Tambahan (isi "-" jika tidak ada)\t: '))
            if extraCode == 'A' or extraCode =='B' or  extraCode =='C' or  extraCode =='-' :
                break
            else :
                print(f'Pilihan Harus Huruf("A,B,C")')
        except :
            print(f'Pilihan Harus Huruf("A,B,C")')
    
    foodPrice = int(food[f'0{foodCode}']['price'])
    drinkPrice = int(drink[f'0{drinkCode}']['price'])
    if extraCode == '-' :
        extraName = '-'
        extraPrice = 0
    else :
        extraName = extra[f'{extraCode}']['name']
        extraPrice = int(extra[f'{extraCode}']['price'])
    subTotal = int(foodPrice + drinkPrice + extraPrice)
    tax = int(subTotal * 0.11)
    totalPrice = int(subTotal + tax)
    
    data = TEMPLATE.copy()
    data['name'] = str(name) + (' '*(100 - len(str(name))))
    data['foodCode'] = str(foodCode)
    data['foodName'] = str(food[f'0{foodCode}']['name']) + (' '*(100 - len(str(food[f'0{foodCode}']['name']))))
    data['foodPrice'] = str(foodPrice) + (' '*(10 - len(str(food[f'0{foodCode}']['price']))))
    data['drinkCode'] = str(drinkCode)
    data['drinkName'] = str(drink[f'0{drinkCode}']['name']) + (' '*(100 - len(str(drink[f'0{drinkCode}']['name']))))
    data['drinkPrice'] = str(drinkPrice) + (' '*(10 - len(str(drink[f'0{drinkCode}']['price']))))
    data['extraCode'] = str(extraCode) 
    data['extraName'] = str(extraName) + (' '*(100 - len(str(extraName))))
    data['extraPrice'] = str(extraPrice) + (' '*(10 - len(str(extraPrice))))
    data['subTotal'] = str(subTotal) + (' '*(10 - len(str(subTotal))))
    data['tax'] = str(tax) + (' '*(10 - len(str(tax))))
    data['totalPrice'] = str(totalPrice) + (' '*(10 - len(str(totalPrice))))
    
    dataStr = f"{data['name']},{data['foodCode']},{data['foodName']},{data['foodPrice']},{data['drinkCode']},{data['drinkName']},{data['drinkPrice']},{data['extraCode']},{data['extraName']},{data['extraPrice']},{data['subTotal']},{data['tax']},{data['totalPrice']}\n"
    
    try :
        with open(DBNAME, 'a', encoding='utf-8') as file :
            file.write(dataStr)
    except :
        print('Data tidak bisa ditambahkan, database error')
        
def read(**kwargs) :
    try : 
      with open (DBNAME, 'r') as file :
            dataFile = file.readlines()
            # Mengambil data untuk fungsi lain
            if 'userKey' in kwargs :
                indexData = []
                for i, j in enumerate (dataFile) :
                    content = j.split(',')
                    for k in content :
                        if kwargs['userKey'] in str.lower(k) :
                            indexData.append(i)
                return indexData
            elif 'dataRaw' in kwargs :
                return dataFile
            elif 'index' in kwargs :
                return dataFile[kwargs['index']]
            elif 'dataLength' in kwargs :
                return len(dataFile)
            
        
    except :
        pesan = f"Database Kosong, Silahkan Tambahkan Data"
        return print(f"\n\n{pesan:^145}\n\n{'-'*145}")
    # Header
    NO = 'NO.'
    NAME = 'Nama Pelanggan'
    FOODNAME = 'Nama Makanan'
    DRINKNAME = 'Nama Minuman'
    EXTRANAME = 'Menu Tambahan'
    TOTALPRICE = 'Total Bayar'
    judul = "DAFTAR PEMBAYARAN MAKANAN"
    print(f"{judul:^145}")
    print("="*145)
    print(f"|{NO:<3}|{NAME:<30}|{FOODNAME:<30}|{DRINKNAME:<30}|{EXTRANAME:<30}|{TOTALPRICE:>15}|")
    print("-"*145)
    
    # Body
    
    for index, data in enumerate (dataFile) :
        dataBreak = data.split(',')
        name = dataBreak[0]
        foodName = dataBreak[2]
        drinkName = dataBreak[5]
        extraName = dataBreak[8]
        totalPrice = locale.currency((int(dataBreak[12][:-1])),grouping=True ) [:-3]
        print(f"|{index+1:<3}|{name:.30}|{foodName:.30}|{drinkName:.30}|{extraName:.30}|{totalPrice:>15}|")
            
    
    # Footer  
    print("-"*145)
        
    
def search():
    read()
    while True :
        try :
            userKey = str.lower(input("\n\nMasukan Nama Pelanggan\t: "))
            break
        except :
            print("Nama tidak valid")
    listIndex = read(userKey = userKey)
    if not listIndex :
        print("Data Pelanggan Tidak Ditemukan")
    else :
        dataRaw = read(dataRaw = True)
        print("-"*145)
        for i in listIndex :
            dataBreak = dataRaw[i].split(',')
            name = dataBreak[0]
            foodName = str(dataBreak[2]).strip()
            drinkName = str(dataBreak[5]).strip()
            extraName = dataBreak[8]
            totalPrice = locale.currency((int(dataBreak[12][:-1])),grouping=True ) [:-3]
            package = f"{foodName} + {drinkName}"
            print(f"|{i+1:<3}|{name:.30}|{package:61}|{extraName:.30}|{totalPrice:>15}|")
        print("-"*145)
        
            
def update():
    read()
    dataLength = read(dataLength = True)
    while True:
        try :
            userOption = int(input('Pilih No Pelanggan\t: '))
            if userOption <= dataLength and userOption > 0 :
                break
            else :
                print("No Pelanggan Tidak Ditemukan")
        except :
            print(f"Pilihan Angka (1-{dataLength}")
        
    userData = read(index = userOption - 1)
    dataBreak = userData.split(',')
    name = dataBreak[0]
    foodCode = dataBreak[1]
    foodName = dataBreak[2].strip()
    foodPrice = dataBreak[3].strip()
    drinkCode = dataBreak[4]
    drinkName = dataBreak[5].strip()
    drinkPrice = dataBreak[6].strip()
    extraCode = dataBreak[7]
    extraName = dataBreak[8].strip()
    extraPrice = dataBreak[9].strip()
    print(f"\n1. Nama Pelanggan\t: {name}\n2. Nama Makanan\t\t: {foodName}\n3. Nama Minuman\t\t: {drinkName}\n4. Menu Tambahan\t: {extraName}")
    while True :
        try :
            userUpdate = int(input("Pilih data yang akan diubah\t: "))
            if userUpdate <= 4 and userUpdate > 0 :
                break
            else :
                print("Pilihan tidak ada (1-4)")
        except :
            print("Pilihan harus angka (1-4)")
    match userUpdate :
        case 1 :
            name = input("Nama Pelanggan\t: ")
        case 2 :
            while True :
                try :
                    foodCode = int(input('Kode Makanan\t\t\t: '))
                    if foodCode <= len(food) and foodCode > 0 :
                        break
                    else :
                        print('Data Makanan Tidak Ditemukan')
                except :
                    print(f"Pilihan Harus Angka 01 - 0{len(food)} ")
            foodName = str(food[f'0{foodCode}']['name'])
            foodPrice = int(food[f'0{foodCode}']['price'])
        case 3 : 
            while True :
                try :
                    drinkCode = int(input('Kode Minuman\t\t\t: '))
                    if drinkCode <= len(drink) and drinkCode > 0 :
                        break
                    else :
                        print('Data Makanan Tidak Ditemukan')
                except :
                    print(f"Pilihan Harus Angka 01 - 0{len(drink)} ")
            drinkName = str(drink[f'0{drinkCode}']['name'])
            drinkPrice = int(drink[f'0{drinkCode}']['price'])
        case 4 : 
            while True :
                try :
                    extraCode = str.upper(input('Kode Menu Tambahan (isi "-" jika tidak ada)\t: '))
                    if extraCode == 'A' or extraCode =='B' or  extraCode =='C' or  extraCode =='-' :
                        break
                    else :
                        print(f'Pilihan Harus Huruf("A,B,C")')
                except :
                    print(f'Pilihan Harus Huruf("A,B,C")')
                if extraCode == '-' :
                    extraName = '-'
                    extraPrice = 0
                else :
                    extraName = extra[f'{extraCode}']['name']
                    extraPrice = int(extra[f'{extraCode}']['price'])
                    
    subTotal = int(foodPrice) + int(drinkPrice) + int(extraPrice)
    tax = int(subTotal * 0.11)
    totalPrice = int(subTotal + tax)
    
    data = TEMPLATE.copy()
    data['name'] = str(name) + (' '*(100 - len(str(name))))
    data['foodCode'] = str(foodCode)
    data['foodName'] = str(food[f'0{foodCode}']['name']) + (' '*(100 - len(str(food[f'0{foodCode}']['name']))))
    data['foodPrice'] = str(foodPrice) + (' '*(10 - len(str(food[f'0{foodCode}']['price']))))
    data['drinkCode'] = str(drinkCode)
    data['drinkName'] = str(drink[f'0{drinkCode}']['name']) + (' '*(100 - len(str(drink[f'0{drinkCode}']['name']))))
    data['drinkPrice'] = str(drinkPrice) + (' '*(10 - len(str(drink[f'0{drinkCode}']['price']))))
    data['extraCode'] = str(extraCode) 
    data['extraName'] = str(extraName) + (' '*(100 - len(str(extraName))))
    data['extraPrice'] = str(extraPrice) + (' '*(10 - len(str(extraPrice))))
    data['subTotal'] = str(subTotal) + (' '*(10 - len(str(subTotal))))
    data['tax'] = str(tax) + (' '*(10 - len(str(tax))))
    data['totalPrice'] = str(totalPrice) + (' '*(10 - len(str(totalPrice))))
    
    dataStr = f"{data['name']},{data['foodCode']},{data['foodName']},{data['foodPrice']},{data['drinkCode']},{data['drinkName']},{data['drinkPrice']},{data['extraCode']},{data['extraName']},{data['extraPrice']},{data['subTotal']},{data['tax']},{data['totalPrice']}\n"
    
    
    # seek 
    lengthDataStr = len(dataStr)
    dataSeek = lengthDataStr*(userOption-1) + (userOption-1)
    
    try :
        with open(DBNAME, 'r+', encoding='utf-8') as file :
            file.seek(dataSeek)
            file.write(dataStr)
    except :
        print("Gagal Mengubah Data, Database error")
    
            
        
            
def delete():
    read()
    dataLength = read(dataLength = True)
    while True :
        try :
            delOption = int(input(f"Pilih nomor yang akan dihapus (1 - {dataLength}) : ")) - 1
            if delOption <= dataLength and delOption >= 0 :
                break 
            else :
                print("Nomor tidak ditemukan")
        except :
            print("Pilihan harus angka")
    content = read(dataRaw = True)
    for i, data in enumerate (content) :
        if i == delOption :
            pass
        else :
            try :
                with open ('dataTemp.txt', 'a', encoding='utf-8') as file :
                    file.write(data)
            except :
                print('Database error')
    os.remove(DBNAME)
    os.rename('dataTemp.txt', DBNAME)

        
        