def first(word):
    return word[0]
    #Bu fonksiyon aslında birinci listede
    # birinci eleman olan elemaının 0'ıncı
    # elemanını getirir.
#map fonksiyonu ise aslında listedeki
#her elemanı tek tek kontrol ederek onun\
#verilen fonksiyona bağlı olarak işlemlerini
#gerçekleştirir.
words=["I am, ","mine ","real ","artifical ","casting ","intellegence ","side ","theory!"]
acro2= list(map(first,words))
print(acro2)
acro =""
#join komutu çıktıları birbirine bağlar
acro = acro.join(acro2).upper()
print(acro)
