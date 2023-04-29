#KullaniciAdi: Emircan
#Sife : 1221803014  

tumKurslar = ["[1].Csharp Egitimi" , "[2].Python Egitimi" , "3.Java Egitimi"]

KayitliKurslar = []

def KurslariGoruntule():

  for kurslar in tumKurslar:
    print(kurslar)

print("Admin Girisi")
kullaniciAdi = input("Kullanici Adi : ")
sifre = input("Sifre : ")

if(kullaniciAdi == "Emircan" and sifre =="1221803014"):
    print("Hos Geldiniz " + kullaniciAdi)
    print("Kurslarim   : [1]")
    print("Tum Kursalr : [2]")
    print("Kariyer     : [3]")

secim=input("Seciminiz :")
print("***")

if secim == "1":
  print("Kayıtlı kursunuz bulunamamıstir..")

elif secim == "2":
  KurslariGoruntule()
kurs_secim = input("Kayıt yaptırmak istediğiniz kursun numarasını giriniz : ")

if kurs_secim == "1":
  print("1 numaralı kursa kaydınız oluşturulmuştur !")

elif kurs_secim == "2":
  print("2 numaralı kursa kaydınız oluşturulmuştur !")

elif kurs_secim == "3":
  print("3 numaralı kursa kaydınız oluşturulmuştur !")

else:
  print("Kullanci adi veya sifre hatali !!") 

  