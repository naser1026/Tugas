
while True :
    try :
        nilai = str.upper(input('Masukan nilai : '))
        break
    except :
        print("Nilai harus huruf")
match nilai :
    case 'A-' : print("Nilai Sangat Memuaskan")
    case 'B+' : print("Nilai Sudah Baik")
    case 'B' : print("Bisa ditingkatkan lagi")
    case 'C+' : print("Harus diperbaiki lagi")
    case 'C' : print("Buruk")
    case 'D' : print("Sangat Buruk")
    case 'E' : print("Harus Mengulang")
    case __ : print("Nilai diluar range")