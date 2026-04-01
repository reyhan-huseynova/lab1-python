#listin daxilinde de list ola biler
#eksine index intervalinda step yazilmalidir
'''n=int(input("enter the length:"))
a=[i for i in range (n)] #ardicil doldurur
print(a)'''

'''n=int(input("enter the length:"))
for i in range (n):
    a=a+[i] #a+=[i]
print(a)'''

'''n=int(input("enter the length:"))
a=[i for i in range (0, n, 2)]
print(a)'''

#user ededleri ozu daxil edir
'''n=int(input("enter the length:"))
a=[int(input()) for i in range(n)]
print(a)'''

'''n=int(input("enter the length:"))
from random import*
#* yerine randint yazsaq randomdan yalniz integer cagirir az yer tutur
a=[randint(10,100) for i in range(n)]
print(a)
count=0
for i in a:
    if i%2==0:
        count+=1
        print(i)
print(count)'''

#indexleri gosterir
'''n=int(input("enter the length:"))
from random import*
a=[randint(10,100) for i in range(n)]
for i in range (len(a)):
    print(a[i], i)'''

#cut elementler ve indexleri
'''n=int(input("enter the length:"))
from random import*
a=[randint(10,100) for i in range(n)]
for i in range (len(a)):
    if a[i]%2==0:
        print(a[i], i)''' #natamam

#exercise a (ededi orta)
'''n=int(input("enter the length:"))
summ=0
from random import*
a=[randint(10,100) for i in range(n)]
print(a)
for i in a:
    summ+=i
orta=summ/len(a)
print(orta)''' #1 defe cixsin deye fordan kenarda

#exercise b (50den kicik ve boyuklerin average)
'''n=int(input("enter the length:"))
summ1=0
summ2=0
count1=0
count2=0
from random import*
a=[randint(0,100) for i in range(n)]
print(a)
for i in a:
    if i<50:
        summ1+=i
        count1+=1
    else:
        summ2+=i
        count2+=1 
orta1=summ1/count1
orta2=summ2/count2
print(orta1, orta2)'''

#exercise c (1,N) intervalinda ele random olsun ki butun integerler bir defe olsun
'''m=int(input("enter the length:")) #goal listin uzunlugu
a=[]
from random import*
while len(a)<m : #randomlarin sayi goal listin uzn. beraber olanda dayanir
    k=randint(1,m)
    print(k)
    if k not in a:
        a+=[k] #append
print(a)'''

#axtarilan eded ve index(ler)i
'''n=int(input("enter the length:"))
m=int(input("enter a number:"))
flag=0
from random import*
a=[randint(0,5) for i in range(n)]
print(a)
for i in range(len(a)):
    if a[i] == m:
        print(a[i], i)
        flag=1
if flag==0: #yoxlayanda 2 beraber olur
    print("not in this list")'''

#yanasi tekrar ededleri mueyyen etmek
'''n=int(input("enter the length:"))
flag=0
from random import*
a=[randint(0,5) for i in range(n)]
print(a)
for i in range(len(a)-1): #index cixarmaq isteyende
    if a[i]==a[i+1]:
        print(a[i], i)
        flag=1
if flag==0:
    print("not in this list")'''

#max eded ve sayi
'''n=int(input("enter the length:"))
x=int(input("enter the first number:"))
a=[]
maxx=x
count=1
a=a+[x]
for i in range(1, n):
    x=int(input()) #listi user doldurur
    a+=[x]
    if maxx==x: #input ve maxx-in dovrde muqayisesi
        count+=1
    elif maxx<x:
        maxx=x
        count=1
print("max:", maxx)
print("count:", count)'''

#sonuncu eded 1ci olur ve qalan hissenin yerleri deyisir
'''from random import*
n=int(input("enter the length:"))
a=[randint(0,5) for i in range(n)]
print(a)
#new=a[-1::]+a[0:-1] #cut-cut deyisir
new=a[1::]+a[:1] #hamisi bir index surusur
print(new)'''












































































