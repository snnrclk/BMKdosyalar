# for =>list: Bir liste üzerinde çalıştığımızda liste elemanlarına ve listenin farklı özelliklerine erişmek için kullanırız. liste=dizi
#while =>koşullu: Belli bir koşul sağlandığı sürece devam eder, döngünün kesintisiz devam edebilmesi için o koşulun sağlanması gerekir.

# en çok for while döngüsü lazım oluyor.

sayilar = [1,2,3,4,6,8,91,21]
isimler = ["Ali", "Ahmet", "Zeynep"]
adSoyad = "Abdullah Göktaş"

# print(sayilar[0])
# print(sayilar[1])
# print(sayilar[2])
# print(sayilar[3])
# print(sayilar[4]) #çok kod yazmak gerekecek.

for x in sayilar: #sayilar ın değişkenini başka bir şeyin değişkenine verme. Hepsi kendisine özel.
    print(x)

# x = sırayla liste elemanları 
# printte ne işlem yapmak istersem onu yaptırıyorum.

for isim in isimler:
    print("Merhaba "+isim)


# Bazen de listenin eleman sayısı kadar bir şey yazdırıcam. Yazdırma sayısı eleman sayısına eşit.
for x in sayilar:
    print("Merhaba BMK")

for isim in isimler:
    print(isim)

for i in adSoyad:
    print(i)


my_dict = {
    "41":"Kocaeli",
    "53":"Rize" ,
    "35":"İzmir",
}

for x in my_dict:
    print(my_dict[x])

for x in my_dict.values():
    print(x)

for x in my_dict.keys(): # x lere karşılık gelene bak ve keyleri yazdır
    print(x)

for x in my_dict.items():
    print(x)

# Metotlarda parantez aç kapa. Parametre yazmana gerek yok. 

# Koşullarda hep parantez olacak : if ve while (for da yok.) (Metotlardaki aç kapa parantezinden bahsetmiyorum.)


sayilar = [1,2,3,4,5,6,7,8,9]
#while => koşullu

while (True):
    print("Merhaba")

i=1 # i ye kaç verirsen oradan başlicak.

while i <= 10:  # i 1 den başlicak 9 dan küçük olacak şekilde gösterecek, devam edecek.
    print(i)
    i += 1

i=0

while (i < len(sayilar)):  #len(sayilar)=9 
    print(sayilar[i])
    i+=1    # i yi 1 arttır 9<= desem 9. indeks yok o yüzden = demedim.

for sayi in sayilar:
    print(sayi)

