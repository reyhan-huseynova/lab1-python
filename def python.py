#armstrong ededler (dovr ile)
'''n=int(input())
count=0
copy=n
copy2=n
yekun=0
while n>0 :
    count=count+1 #reqemler silindikce artir
    n=n//10
while copy>0 :
    yekun+=(copy%10)**count
    copy=copy//10
if copy2==yekun :
    print("armstrong")
#count=1,2,3 ; n=153->15,1,0'''

#armstrong ededler (funksiya ile)
'''#return print kimi dovre girmeyib 1 defe cixir
def reqem_sayi(x) :
    count=0
    while x>0 :
        count+=1
        x=x//10
    return count #ededin uzunlugunu cixarir
#y=int(input())
#print(reqem_sayi(y))

def armstrong(x): #ic-ice funksiya
#def ozunden evvelki deyisenleri gormur
#return kodu kesir (oz altindaki hisseni)
    copy=x
    yekun=0
    copy2=x
    while copy>0 :
        yekun+=(copy%10)**reqem_sayi(x)
        copy=copy//10
    ##return yekun
#y=int(input())
#print(armstrong(y))
    if copy2==yekun :
        return True
    else:
        return False
    #if else evezine "return yekun==copy2"
for i in range (1,10000):
    if armstrong(i)==True:
        print(i, "armstrong")'''

#-1 inserte qeder ededlerin ceminin cut tek olmasi
'''def f():
    eded=0
    cem=0
    while True :
        eded=int(input())
        if eded==-1 :
            break
        cem+=eded
    if cem%2==0:
        return "cut"
    else:
        return "tek"
print(f())'''

#a-nin b-ye bolunmesini yoxlamaq
'''def f(a,b):
    if a%b==0:
        return True
a=int(input())
b=int(input())
print(f(a,b))'''

#curzon ededleri (2^n+1=2n+1)
'''def curzon(n):
    if (2**n+1)%(2*n+1)==0 :
        return True
for i in range (1,100):
    if curzon(i)==True :
        print(i)'''

#n^n=k olarsa true
'''def f(n,k):
    if n**n==k:
        return True
n=int(input())
k=int(input())'''

#pronic ededler (qonsu ededlerin hasili)
'''def pronic(p):
    for i in range (1,p+1):
        if p==i*(i+1):
            return True
for i in range (1,100):
    if pronic(i)==True:
        print(i)'''

#ededin uzunlugu
'''def f(x):
    x=abs(x) #menfi ededlercun de
    counter=0
    while x>0:
        counter+=1
        x=x//10
    return counter
a=int(input())
print(f(a))'''

#disarium ededler
'''def count(x):
    c=0 #count
    while x>0:
        c+=1
        x=x//10
    return c
def disarium(n):
    yekun=0
    copy=n
    while n>0:
        yekun+=(n%10)**(count(n))
        n=n//10
    return yekun==copy
for i in range (1, 100):
    if disarium(i):
        print(i)'''

#moran ededler (eded oz reqemleri cemine bolunur)
def moran(a):
    copy=a
    summ=0
    while a>0:
        a=a//10
        summ+=a
    return summ
a=int(input())
if copy%summ==0 :
    print("bolunur")
    














































