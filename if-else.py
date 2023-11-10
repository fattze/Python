# 1 - kullanıcıdan isim,yaş ve eğitim biilgilerini isteyip ehliyet alabilme durumunu kontrol et.
#Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır. 

name=input("isim giriniz:")
age=int(input("yaş giriniz:"))
education=input("eğitim bilgisi giriniz:")
if (age>=18):
    if (education=='lise') or (education=='üniversıte'):
        print(" ehliyet alabilir.")
    else:
        print(f'{name} ehliyet alamazsınız egitim bilgileriniz tutmuyor')
else:
    print(f'{name} ehliyet alamazsınız yaşınız tutmuyor.') 

#2- bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#0-24=>0
#25-44=>1
#45-54=>2
#55-69=>3
#70-84=>4
#85-100=>5

yazılı1=int(input('yazılı1 gir:'))
yazılı2=int(input('yazılı2 gir:'))
sözlü=int(input('sözlü gir:'))
ort=int((yazılı1 + yazılı2+ sözlü)/3)
if (ort==0) and (ort<=24):
    print('notun 0')
elif (ort>=25)and (ort<=44):
    print('notun 1')
elif (ort>=45)and(ort<=54):
    print('notun 2')
elif (ort>=55)and (ort<=69):
    print('notun 3')
elif (ort>=70)and (ort<=84):
    print('notun 4')
elif (ort>=85) and (ort<=100):
    print('notun 5')
else:
    print('geçerli bir not gir.')



#



