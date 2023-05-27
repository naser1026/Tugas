import locale
import os
import string
import random
import time

def clear() :
    if os.name == 'nt' :
        return(os.system('cls'))
    else :
        return(os.system('clear'))
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
    while True :
        clear()
        print('-'*50)
        print("Masukan Data Pesanan")
        name = input('\nNama Pelanggan\t\t\t: ')
        while True :
            clear()
            print("Masukan Data Pesanan \n")
            try :
                foodMenu()
                foodCode = int(input('Kode Makanan\t\t\t: '))
                if foodCode <= len(food) and foodCode > 0 :
                    if foodCode < 10 :
                        foodCode = str(f"0{foodCode}")
                    else :
                        foodCode = str(foodCode)
                    break
                else :
                    print(f'Data Makanan Tidak Ditemukan (01 - {len(food)})')
                    os.system('pause')
            except :
                print(f"Pilihan Harus Angka (01 - {len(food)})")
                os.system('pause')
        while True :
            clear()
            print("Masukan Data Pesanan \n")
            try :
                drinkMenu()
                drinkCode = int(input('Kode Minuman\t\t\t: '))
                if drinkCode <= len(drink) and drinkCode > 0 :
                    break
                else :
                    print(f'Data Makanan Tidak Ditemukan (01 - 0{len(drink)})')
                    os.system('pause')
            except :
                print(f"Pilihan Harus Angka (01 - 0{len(drink)}) ")
                os.system('pause')
        while True :
            clear()
            print("Masukan Data Pesanan \n")
            try :
                extraMenu()
                extraCode = str.upper(input('Kode Menu Tambahan (isi "-" jika tidak ada)\t: '))
                if extraCode == 'A' or extraCode =='B' or  extraCode =='C' or  extraCode =='-' :
                    break
                else :
                    print(f'Pilihan Harus Huruf("A,B,C")')
                    os.system('pause')
            except :
                print(f'Pilihan Harus Huruf("A,B,C")')
                os.system('pause')
        
        foodPrice = int(food[foodCode]['price'])
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
        pk = "".join(random.choice(string.ascii_letters) for i in range(6))
        dateAdd = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
        
        data = TEMPLATE.copy()
        data['name'] = str(name) + (' '*(100 - len(str(name))))
        data['foodCode'] = str(foodCode)
        data['foodName'] = str(food[str(foodCode)]['name']) + (' '*(100 - len(str(food[foodCode]['name']))))
        data['foodPrice'] = str(foodPrice) + (' '*(10 - len(str(food[foodCode]['price']))))
        data['drinkCode'] = str(drinkCode)
        data['drinkName'] = str(drink[f'0{drinkCode}']['name']) + (' '*(100 - len(str(drink[f'0{drinkCode}']['name']))))
        data['drinkPrice'] = str(drinkPrice) + (' '*(10 - len(str(drink[f'0{drinkCode}']['price']))))
        data['extraCode'] = str(extraCode) 
        data['extraName'] = str(extraName) + (' '*(100 - len(str(extraName))))
        data['extraPrice'] = str(extraPrice) + (' '*(10 - len(str(extraPrice))))
        data['subTotal'] = str(subTotal) + (' '*(10 - len(str(subTotal))))
        data['tax'] = str(tax) + (' '*(10 - len(str(tax))))
        data['totalPrice'] = str(totalPrice) + (' '*(10 - len(str(totalPrice))))
        data['pk'] = str(pk)
        data['dateAdd'] = str(dateAdd)
        
        dataStr = f"{data['name']},{data['foodCode']},{data['foodName']},{data['foodPrice']},{data['drinkCode']},{data['drinkName']},{data['drinkPrice']},{data['extraCode']},{data['extraName']},{data['extraPrice']},{data['subTotal']},{data['tax']},{data['totalPrice']},{data['pk']},{data['dateAdd']}\n"
        
        orderDetails(data['pk'], data['dateAdd'], data['name'],data['foodCode'],data['foodName'],data['foodPrice'],data['drinkCode'],data['drinkName'],data['drinkPrice'],data['extraCode'],data['extraName'],data['extraPrice'],data['subTotal'],data['tax'],data['totalPrice'])
        
        isDone = str.lower(input("Apakah Pesanan Sudah Sesuai (y/n)? "))
        if isDone == 'y' :
            break
    
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
                    for k, l in enumerate (content) :
                        if k == 0 or k % 13 == 0 :
                            if kwargs['userKey'] in str.lower(l) :
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
        return False
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
    print(f"|{NO:<3}|{NAME:<30}|{FOODNAME:<30}|{DRINKNAME:<30}|{EXTRANAME:<30}|{TOTALPRICE:<15}|")
    print("-"*145)
    
    # Body
    for index, data in enumerate (dataFile) :
        dataBreak = data.split(',')
        name = dataBreak[0]
        foodName = dataBreak[2]
        drinkName = dataBreak[5]
        extraName = dataBreak[8]
        totalPrice = locale.currency((int(dataBreak[12])),grouping=True ) [:-3]
        print(f"|{index+1:<3}|{name:.30}|{foodName:.30}|{drinkName:.30}|{extraName:.30}|{totalPrice:>15}|")
        print("-"*145)
    os.system('pause')
        
    
def search():
    if read() == False :
        return False
    while True :
        try :
            userKey = str.lower(input("\n\nMasukan Nama Pelanggan\t: "))
            break
        except :
            print("Nama tidak valid")
    listIndex = read(userKey = userKey)
    if not listIndex :
        print("Data Pelanggan Tidak Ditemukan")
        os.system('pause')
    else :
        dataRaw = read(dataRaw = True)
        print("-"*145)
        for i in listIndex :
            dataBreak = dataRaw[i].split(',')
            name = dataBreak[0]
            foodName = str(dataBreak[2]).strip()
            drinkName = str(dataBreak[5]).strip()
            extraName = dataBreak[8]
            totalPrice = locale.currency((int(dataBreak[12])),grouping=True ) [:-3]
            package = f"{foodName} + {drinkName}"
            print(f"|{i+1:<3}|{name:.30}|{package:61}|{extraName:.30}|{totalPrice:>15}|")
        print("-"*145)
        os.system('pause')
        
            
def update():
    if read() == False :
        return False
    dataLength = read(dataLength = True)
    while True:
        try :
            print("-"*64)
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
    while True :
        print(f"\n1. Nama Pelanggan\t: {name}\n2. Nama Makanan\t\t: {foodName}\n3. Nama Minuman\t\t: {drinkName}\n4. Menu Tambahan\t: {extraName}")
        while True :
            try :
                userUpdate = int(input("\nPilih data yang akan diubah\t: "))
                print("-"*64)
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
                        foodMenu()
                        foodCode = int(input('Kode Makanan\t: '))
                        if foodCode <= len(food) and foodCode > 0 :
                            if foodCode < 10 :
                                foodCode = str(f"0{foodCode}")
                            else :
                                foodCode = str(foodCode)
                            break
                        else :
                            print('Data Makanan Tidak Ditemukan')
                    except :
                        print(f"Pilihan Harus Angka 01 - 0{len(food)} ")
                foodName = str(food[foodCode]['name'])
                foodPrice = int(food[foodCode]['price'])
            case 3 : 
                while True :
                    try :
                        drinkMenu()
                        drinkCode = int(input('Kode Minuman\t: '))
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
                        extraMenu()
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
        pk = "".join(random.choice(string.ascii_letters) for i in range(6))
        dateAdd = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime())
        
        data = TEMPLATE.copy()
        data['name'] = str(name) + (' '*(100 - len(str(name))))
        data['foodCode'] = str(foodCode)
        data['foodName'] = str(foodName) + (' '*(100 - len(str(foodName))))
        data['foodPrice'] = str(foodPrice) + (' '*(10 - len(str(foodPrice))))
        data['drinkCode'] = str(drinkCode)
        data['drinkName'] = str(drink[f'0{drinkCode}']['name']) + (' '*(100 - len(str(drink[f'0{drinkCode}']['name']))))
        data['drinkPrice'] = str(drinkPrice) + (' '*(10 - len(str(drink[f'0{drinkCode}']['price']))))
        data['extraCode'] = str(extraCode) 
        data['extraName'] = str(extraName) + (' '*(100 - len(str(extraName))))
        data['extraPrice'] = str(extraPrice) + (' '*(10 - len(str(extraPrice))))
        data['subTotal'] = str(subTotal) + (' '*(10 - len(str(subTotal))))
        data['tax'] = str(tax) + (' '*(10 - len(str(tax))))
        data['totalPrice'] = str(totalPrice) + (' '*(10 - len(str(totalPrice))))
        data['pk'] = str(pk)
        data['dateAdd'] = str(dateAdd)
        
        dataStr = f"{data['name']},{data['foodCode']},{data['foodName']},{data['foodPrice']},{data['drinkCode']},{data['drinkName']},{data['drinkPrice']},{data['extraCode']},{data['extraName']},{data['extraPrice']},{data['subTotal']},{data['tax']},{data['totalPrice']},{data['pk']},{data['dateAdd']}\n"
        
        
        # seek 
        lengthDataStr = len(dataStr)
        index = userOption - 1
        dataSeek = lengthDataStr*index + index
        
        try :
            with open(DBNAME, 'r+', encoding='utf-8') as file :
                file.seek(dataSeek)
                file.write(dataStr)
        except :
            print("Gagal Mengubah Data, Database error")
            os.system('pause')

        print("\nData Berhasil Diubah")
        read()
        isDone = str.lower(input("Apakah Sudah Sesuai (y/n)? "))
        if isDone == 'y' :
            break
        
            
def delete():
    if read() == False :
        return False
    dataLength = read(dataLength = True)
    while True :
        try :
            delOption = int(input(f"Pilih pelanggan yang akan dihapus (1 - {dataLength}) : ")) - 1
            if delOption < dataLength and delOption >= 0 :
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
                os.system('pause')
                
    os.remove(DBNAME)
    os.rename('dataTemp.txt', DBNAME)
    print("Data berhasil dihapus")
    read()

def foodMenu() :
    # Header
    print(f"{'Menu Makanan':^64}")
    CODE = 'Kode Makanan'
    FOODNAME = 'Nama Makanan'
    FOODPRICE = 'Harga Makanan'
    print('-'*64)
    print(f"|{CODE:^20}|{FOODNAME:20}|{FOODPRICE:20}|")
    print('-'*64)
    
    # Body
    for i in range(1,len(food)+1) :
        if i < 10 : 
            code = f"0{i}"
        else :
            code = str(i)
        foodName = food[code]['name']
        foodPrice = food[code]['price']
        foodPrice = locale.currency((int(foodPrice)),grouping=True ) [:-3]
        print(f"|{code:^20}|{foodName:20}|{foodPrice:>20}|")
        print('-'*64)
        
def drinkMenu() :
    # Header
    print(f"\n{'Menu Minuman':^64}")
    CODE = 'Kode Minuman'
    DRINKNAME = 'Nama Minuman'
    DRINKPRICE = 'Harga Minuman'
    print('-'*64)
    print(f"|{CODE:^20}|{DRINKNAME:20}|{DRINKPRICE:20}|")
    print('-'*64)
    
    # Body
    for i in range(1,len(drink)+1) :
        if i < 10 : 
            code = f"0{i}"
        else :
            code = str(i)
        drinkname = drink[code]['name']
        drinkPrice = drink[code]['price']
        drinkPrice = locale.currency((int(drinkPrice)),grouping=True ) [:-3]
        print(f"|{code:^20}|{drinkname:20}|{drinkPrice:>20}|")
        print('-'*64)
        
def extraMenu() :
    # Header
    print(f"\n{'Menu Tambahan':^64}")
    CODE = 'Kode Menu Tambahan'
    EXTRANAME = 'Nama Menu Tambahan'
    EXTRAPRICE = 'Harga Menu Tambahan'
    print('-'*64)
    print(f"|{CODE:^20}|{EXTRANAME:20}|{EXTRAPRICE:20}|")
    print('-'*64)
    
    # Body
    for i in range(1,len(extra)+1) :
        code = chr(64 + i)
        extraName = extra[code]['name']
        extraPrice = extra[code]['price']
        extraPrice = locale.currency((int(extraPrice)),grouping=True ) [:-3]
        print(f"|{code:^20}|{extraName:20}|{extraPrice:>20}|")
        print('-'*64)
        
def orderDetails(pk,dateAdd, name, foodCode, foodName, foodPrice, drinkCode, drinkName, drinkPrice, extraCode, extraName, extraPrice, subtotal, tax, totalprice, ) :
    clear()
    foodPrice = locale.currency((int(foodPrice)), grouping=True) [:-3]
    drinkPrice = locale.currency((int(drinkPrice)), grouping=True) [:-3]
    extraPrice = locale.currency((int(extraPrice)), grouping=True) [:-3]
    subtotal = locale.currency((int(subtotal)), grouping=True) [:-3]
    tax = locale.currency((int(tax)), grouping=True) [:-3]
    totalprice = locale.currency((int(totalprice)), grouping=True) [:-3]
    print("="*102)
    print(f"|{'DETAIL PESANAN':100}|")
    print("-"*102)
    print(f"|{'id':28}|: {pk:69}|")
    print("-"*102)    
    print(f"|{'Tanggal Penambahan':28}|: {dateAdd:69}|")
    print("-"*102)    
    print(f"|{'Nama Pelanggan':28}|: {name:.69}|")
    print("-"*102)    
    print(f"|{'Kode Makanan':28}|: {foodCode:69}|")
    print("-"*102)    
    print(f"|{'Nama Makanan':28}|: {foodName:.69}|")
    print("-"*102)    
    print(f"|{'Harga Makanan':28}|: {foodPrice:69}|")
    print("-"*102)     
    print(f"|{'Kode Minuman':28}|: 0{drinkCode:68}|")
    print("-"*102)    
    print(f"|{'Nama Minuman':28}|: {drinkName:.69}|")
    print("-"*102)    
    print(f"|{'Harga Minuman':28}|: {drinkPrice:69}|")
    print("-"*102)     
    print(f"|{'Kode Menu Tambahan':28}|: {extraCode:69}|")
    print("-"*102)    
    print(f"|{'Nama Menu Tambahan':28}|: {extraName:.69}|")
    print("-"*102)    
    print(f"|{'Harga Menu Tambahan':28}|: {extraPrice:69}|")
    print("-"*102)
    print(f"|{'Jumlah Bayar':28}|: {subtotal:69}|")
    print("-"*102)
    print(f"|{'PPN 11%':28}|: {tax:69}|")
    print("-"*102)
    print(f"|{'Total Bayar':28}|: {totalprice:69}|")
    print("="*102)
         
    
        
        
        