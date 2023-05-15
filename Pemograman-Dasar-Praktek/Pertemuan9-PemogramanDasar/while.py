import time

def main() :
    i = 0
    while i <= 5 :
        print(f"i={i}: Python")
        i += 1
        print(f"nilai i berubah menjadi {i}")
        
        time.sleep(60) #Memberi jeda waktu 60 detik
        
if __name__ == '__main__' :
    main()
    