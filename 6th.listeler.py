#Listeler aynı türden verileri saklar. İsim=metinsel=strink=tırnak içinde yazılır.
sayilar=[1,2,3,4,5]
isimler=["Ali","Mehmet","Ayşe"]

#Type parantezinin içine ne yazarsan onun tipini, türünü verir.
print(type(sayilar))
print(type(sayilar[0]))

print(type(isimler))
print(type(isimler[0]))

#Listedeki her elemanın bir indeksi olur.
#İndeks numaraları baştan 0 ile başlar. Ali 0 Mehmet 1 gibi. Eğer sayı lstenin sonlarında ise sondan -1 ile başlar. Ayşe -1 Mehmet -2 gibi.

print(isimler[0])
#İndeksini böyle gösterebiliriz. 0. indeks 1. elemana gidiyor.

#Phyton önceden aynı türden verileri saklıyordu ama şimdi 10. sürüm ve üzerinde farklı veri tiplerini de saklayabilir.

ogrenci=["Ali","Yılmaz","2200000",60,50,70]
#Okul numarası üzerinden bir işlem yapılmıyor. Bu yüzden str dir. Parantez içinde yazıyoruz.

print(ogrenci[0]+" "+ogrenci[1])
ortalama=(ogrenci[3]+ogrenci[4]+ogrenci[5])/3
#Parantez içine almazsak işlem önceliğinden yanlış olur.
#Sayısal=int
# int veri tipi
print(ortalama)
print("Ortalamanız:"+str(ortalama))
#print(str+int) ti. Ama str parantezine alarak int i str ye dönüştürdük. Veri dönüşümü yaptık.

ogrenciler=[["Ali","Yılmaz",60,50,70],["Ayşe","Yılmaz",80,50,70]]

print(ogrenciler[0][0])
#ogrenciler deki 0. indeksin 0. indeksi

print(ogrenciler[1][0])