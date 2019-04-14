
def Toplama(x, y):
    return x + y

def Cikarma(x, y):
    return x - y

def Carpma(x, y):
    return x * y

def Bolme(x, y):
    return x / y

print("Lutfen yapmak istediginiz islemi seciniz.")
print("0.Toplama")
print("1.Çıkarma")
print("2.Çarpma")
print("3.Bölme")

islem = input("Seciminizi giriniz:")

s1 = int(input("1. Sayı: "))
s2 = int(input("2. Sayı: "))

if islem == '0':
    print(s1, "+", s2, "=", Toplama(s1, s2))

if islem == '1':
    print(s1, "-", s2, "=", Cikarma(s1, s2))

if islem == '2':
    print(s1, "*", s2, "=", Carpma(s1, s2))

if islem == '3':
   try:
    print(s1, "/", s2, "=", Bolme(s1, s2))
   except ZeroDivisionError:
      print("Herhangi bir sayi 0'a bolunemez!")
else:
    print("Geçersiz Giriş")