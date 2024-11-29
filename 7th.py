programlama_diller=["Pyhton","C#","Java","Javascript"]

#Listelerde güncelleme
programlama_diller[2]="C++"
print(programlama_diller)

sonuc = programlama_diller
sonuc = len(programlama_diller)
#lenght=uzunluk=len Listedeki eleman sayısını verir.

sonuc = programlama_diller+["go","delphi"]

sonuc = "Pyhton" in programlama_diller
sonuc = "React" in programlama_diller
#Liste içinde var mı diye bakıyorum in ile.
#koşul ifadeleri

del programlama_diller[0]
#Listeden silmek için del yapıyorum.

print(programlama_diller)
print(sonuc) 
#En son 14.line ı sonuca eşitlediğim için sonuc false çıkıyor. Önceki eşlediklerimde çıkardı yoksa.