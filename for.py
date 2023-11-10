sayılar=[1,3,5,7,9,12,19,21]

#1- sayılar listesindeki hangi sayılar 3'ün katıdır 
for a in sayılar:
    if (a%3==0):
        print('3 ün katı olan sayılar:' , a )


#2- sayılar listesindeki sayıların toplamı kaçtır 
toplam = 0
for b in sayılar:
    toplam+= b 
print(toplam)

#3- sayılar listesindeki tek sayıların karesini alınız.
for c in sayılar:
    if (c%2==1):
      print('tek sayıların karesi:' ,(c**2) ) 

sehirler= ['kocaeli', 'istanbul', 'ankara', 'izmir', 'rize']
#4-şehirlerden hangileri en fazla 5 karakterlidir 

for a  in sehirler:
    if len(a)<= 5:
        print(a)


urunler=[  
   {'name': 'samsung s6', 'price' : '3000'},
   {'name': 'samsung s7', 'price' : '4000'},
   {'name': 'samsung s8', 'price' : '5000'},
   {'name': 'samsung s9', 'price' : '6000'},
   {'name': 'samsung s10', 'price':'7000'}
]

#5- ürünlerin fiyatlarının toplamı nedir 
toplam=0
for a in urunler:
    toplam += int(a['price'])
    print (toplam)


#6-ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz

for b in urunler:
    fiyat=int(b['price'])
    if (fiyat<=5000):
        print(b['name'])


