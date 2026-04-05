#oop: object-orinented prongraming
#tao lop vat nuoio  (giong mau sac tuoi can nang)
class Vatnuoi (object) :
    def __init__(self,giong="", mausac="", tuoi=0, CanNang=0):
        self.__giong = giong
        self.__mausac = mausac
        self.__tuoi  = tuoi
        self.__CanNang = CanNang

    def __str__(self) -> str:
        return f"Vatnuoi:{self.__giong}, {self.__mausac},{self.__tuoi}, {self.__CanNang} "

    #getter va setter (lay va dat gia tri thuoc tinh )
    #"get"/"set" + ten thuoc tinh

    def getGiong (self):
        return self.__giong
    
    def getMauSac (self):
        return self.__mauSac
    
    def getTuoi (self):
        return self.__tuoi
    
    def getCanNang (self):
        return self.__CanNang
    
    def setGiong (self, giongMoi):
        if giongMoi == "":print("Gia tri khong duoc de trong ")
        else: self.__giong = giongMoi
    
    def setMauSac (self, mauSacMoi):
        if mauSacMoi == "": print("Gia tri khon duoc de trong")      
        else: self.__mausac = mauSacMoi

    def setTuoi (self, tuoiMoi):
        if tuoiMoi < 0 : print("gia tri khong duoc la so am")
        else: self.__tuoi = tuoiMoi

    def setcaNang (self, canNangMoi):
        if canNangMoi < 0 : print("gia tri khong duoc la so am")
        else: self.__cannang = canNangMoi

#tao doi tung
meol = Vatnuoi("meo", "den")
print(meol)

#gan gia tri cho thuoc tinh 
print(meol.getTuoi())
meol.setTuoi(tuoiMoi=2)

meol.setcaNang(canNangMoi= 3.5)
print(meol.getCanNang())

print(meol)