import math

class Titik :
    def __init__(self, nama, x, y) :
        self.nama = nama
        self.x = x
        self.y = y
    
    def ubahNama(self, nama) :
        self.nama = nama
        
    def ubahX(self, x) :
        self.x = x
    
    def ubahY(self, y) :
        self.y = y
        
    def pindah(self, x, y) : 
        self.x = x
        self.y = y
    
    def __repr__(self):
        return '%s(%d,%d)' % (self.nama, self.x, self.y)
    
class Garis :
    def __init__(self, t1, t2) :
        self.titik1 = t1
        self.titik2 = t2
        
    def panjang(self) :
        return math.sqrt(
            ((self.titik2.x - self.titik1.x )** 2) +
            ((self.titik2.y - self.titik1.y )** 2)
        )