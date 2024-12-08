#value types=değer tipleri
x=10
y=20
x=y       #x=20
y=30
print(x, y)

#reference

a=["elma" , "armut"]
b=["portakal" , "mandalina"]

a=b         #adres kopyaladınız

a[0]="üzüm"
print(a, b)

#liste kopyalama
listeA=[10,20]
listeB=listeA.copy()        #1.yöntem #listeB=[10,20]
#python'un tüm metotlarında içi boş olsa bile parantez koyacaksın.
#syntax=söz dizimi
#Bu parametre almıyor. class ve fonksiyonlar parametre alabilir.
listeB[0]=30

print(listeA,listeB)

#numaralarda bir değişiklik olunca birbirlerini etkilemiyorlar ama listede herhangi bir değişiklik olursa birbirlerini etkiliyorlar.

#remove listeden eleman kaldırma / count listedeki eleman sayısını verir. (len gibidir ve alternatiftir.)

#copy demeden direkt birbirlerine eşitlersek aynı iki adresli listelerimiz oluyor ve birinde olan değişiklik diğerini etkiliyor.
#fakat copy şeklinde eşitlersek onun kopyasını yapmış oluyoruz iki farklı adresli listelerimiz oluyor ve bir değişiklik yapıldığında aslını değiştiremiyor.