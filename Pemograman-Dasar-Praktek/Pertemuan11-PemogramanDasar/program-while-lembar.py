print("=================================")
print("PROGRAM HARGA FOTOCOPY PERHALAMAN")
print("=================================")

lembar = 0
rp = 0
hrg = int(input('Masukan harga per lembar = '))
print(f"Harga Fotocopy = RP. {hrg}/lembar")
print('-'*18)
print(f'{"|Lembar":6}|{"Harga(Rp)":9}|')
print('-'*18)
while lembar < 5 :
    rp += hrg
    lembar += 1
    print(f'|{lembar:^6}|{rp:^9}|')
    print('-'*18)   
    
    