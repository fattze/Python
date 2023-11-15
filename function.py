#1- gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def yazdir(kelime,adet):
    print(kelime*adet)

yazdir('tamam',5)
yazdir('tamam\n',5)

#2- kendine gönderilen sınırsız sayıdaki paremetreyi bir listeye çeviren fonksiyonu yazınız.


def listeyecevir(*params):
    liste=[]
    
    for param in params:
        liste.append(param)

    return liste
hazır=listeyecevir(10,3,45,'tamam')
print(hazır)

#3- gönderilen iki sayı arasındaki tüm asal sayıları bulun.

def asalsayilaribul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1): 
        if sayi > 1:
            for i in range (2, sayi):
                if (sayi%i==0):
                  break
            else:
                print (sayi)


sayi1=int(input('sayı1:'))
sayi2=int(input('sayı2:'))
asalsayilaribul(sayi1,sayi2)

#4- kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndürünüz.


def tambolenleribul(sayii):
    tambolenler=[]

    for i in range(2, sayii):
        if (sayii%i==0):
            tambolenler.append(i)
    return tambolenler

print(tambolenleribul(45))

