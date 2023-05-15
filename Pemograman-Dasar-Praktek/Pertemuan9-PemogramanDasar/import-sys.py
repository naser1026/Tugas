import sys

def main():
    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"]
    no = int(input('Masukan no hari [1-7] : '))
    
    if no < 0 or no > 7 :
        print("Nilai yang dimasukan salah.")
        sys.exit(1)
        
    print(hari[no-1])
    
if __name__ == "__main__" :
    main()
