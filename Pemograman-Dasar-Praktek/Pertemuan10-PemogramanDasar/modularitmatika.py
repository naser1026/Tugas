def tambah(a, b) :
    return a + b
def kurang(a, b) :
    return a - b
def kali(a, b) :
    return a * b
def bagi(a, b) :
    if isinstance(a, int) and isinstance(b, int) :
        return a // b
    if isinstance(a, float) or isinstance(b, float) :
        return a / b
    
def sisaBagi(a, b) :
    return a % b

def pangkat(a, b) :
    return a**b