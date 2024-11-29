sehirler=['izmir','istanbul']
plakalar=[35,34]


#key-value
print(plakalar[0],sehirler[0])
print(plakalar[1],sehirler[1])

print(plakalar[sehirler.index('istanbul')])
print(plakalar[sehirler.index('izmir')])

#dictionary
#Spagetti kod: karmaşık kodlar. 2 kodla yazacağını 100 kodla yazıyorsun.

plakalar={
    'kocaeli':41,
    'istanbul':34,
    'izmir':36
}
#İki noktadan önceki tek tırnak ile yazılır. Eşlendiği şey, iki noktadan sonraki ise tırnaksız yazılır.
#Alt alta yazmamızın sebebi görünürlük iyi olsun. Her veri tipinde virgül koy.

plakalar['izmir']=35
#İzmir'in plakasının yanlışlığını düzeltebiliriz.

print(plakalar['kocaeli'])
print(plakalar['istanbul'])
print(plakalar['izmir'])
#İzmir artık 36 olarak değil 35 olarak çıkacak.