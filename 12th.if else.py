email="info@bmk.com"
parola="123456"

if(email=="info@bmk.com"):       #bu çalışmazsa direkt dışarıdaki else gider içerideki if ve else bakmaz.
    if(parola=="123456"):
        print("Login olundu")
    else:
        print("Parola yanlış")        #içerisi çaışmazsa dışardaki else çalışsın.
else:
    print("Email yanlış")

#-----Bu uzun olan-----


email="info@bmk.com"
parola="123456"

if(email !="info@bmk.com"):
    print("email yanlış")
elif(parola !="123456"):
    print("parola yanlış")
else:
    print("login olundu")

#-----Bu kısası-----

#if içindeki doğru ise çalışır yanlış ise çalışmaz ve sonuç olarak bir şey çıkmaz diğerine devam edilir.
#parantezden sonra iki nokta yapılır yoksa kod çalışmaz. 
#else parametre kabul etmiyor.

