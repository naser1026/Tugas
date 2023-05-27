
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
                print("Database Masih Koson