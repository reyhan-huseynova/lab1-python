#1 
'''for i in range (0,11):
    kv=i**2
    print(f"{kv} is the doubkl of {i}")'''

#f string yazmaq imtahanda bal qazandirir

#2 2ye bolunen ededler cemi
'''s=0
for i in range (0,11):
    if i%2==0 :
        s=s+i
print(s)'''

#print ve s dovrden kenarda olmalidir ki, s sifirlanmasin,
'''print son neticeni cixarsin. if-in altinda olsa else-in
yerinde olduguna gore if odense de odenmese de netice print olur (2 defe)'''

#3 (a,b) arasi c-ye bolunen ededler
'''a=int(input())
b=int(input())
c=int(input())
for i in range (a,b+1):
    if i%c==0 :
        print(i)'''

#4 (5,10)da 7 ve 9 istisna ededler
'''for i in range (5,11):
    if i==7 or i==9 :
        continue
    print(i)'''

# 'continue' ignore edir, dovre qaytarir. 'break' dovru kesir

#5 (a,b) arasi cut ve tek eded sayi
'''s1=0
s2=0
a=int(input())
b=int(input())
for i in range (a,b+1):
    if i%2==0 :
        s1+=1
    else:
        s2+=1
print(f"tek ededlerin sayi {s2}, cut ededlerin sayi {s1}")'''

#6 (1,100) arasi random 10 ededin tek ve ya cut olmasi
''' from random import* #random library
for i in range (10): #for daxilinde bir eded yazanda dovrun sayini gosterir
    a=randint(1,101) #library-den random tam eded
    if a%2==0:
        print(f'{a} cutdur')
    else:
        print(f'{a} tekdir')'''

#7 faktorialin tapilmasi
'''a=int(input())
f=1
if a<0:
    print("faktorial yoxdur")
else:
    for i in range (1, a+1):
        f=f*i
    print(f)'''

#8 ededi ardicilliqda hedler cemi
# 1+2/3+4/5+6/7+...+(2n/2n+1) ilk a heddin cemi:
'''a=int(input())
s=1 #1 dustura uygun gelmir deye ceme atdiq
for i in range (1,a): #a cunki 1ci hedd ele s-dir
    s=s+(2*i)/(2*i+1)
print(s)'''

#faktoriallar cemi
'''a=int(input())
s=0
f=1
for i in range (1,a+1): #dovr 1den baslasin ki f sifirlanmasin
    f=f*i
    #s+=f
    s=s+f
print(s)'''

#1-1/2+1/6-1/24+1/120+...+ ((-1)**k+1)*1/k!
'''a=int(input())
s=0
f=1
for i in range (1,a+1):
    f=f*i
    s=s+((-1)**(i+1))*1/(f) #i+1 cunki i f-e gore 1den baslamalidir
print(s)'''

#polindrom ededin tapilmasi
#mes. 1221=(1*10**3)+(2*10**2)+(2*10**1)+(1*10**0)
'''a=int(input())
yeni=0
copy=a
while a>0: #ve ya while a (a movcud olduqca)
    digit=a%10
    yeni=(yeni*10)+digit
    a=a//10
if copy==yeni :
    print("polindromdur")
else :
    print("polindrom deyil")'''
    
#axirda a sifirlanir deye copy lazim olur yeni ile muqayise ucun
# a : 1221, 1221//10=122, 122//10=12, 12//10=1, 1//10=0
# yeni : 0, 0*10+1, 1*10+1, 12*10+2, 122*10+1
# digit : %10 -> 1, 2, 2, 1, 0
# ededin reqemlerine aid misallarda adeten while lazim olur

#bolenlerin tapilmasi:
'''a=int(input())
for i in range (1,a+1):
    if a%i==0:
        print(i)
ve ya

a=int(input())
i=1
say=0
while i<=a :
    if a%i==0:
        say=say+1
        print(i)
    i=i+1
print (f"{a} ededinin bolenleri sayi {say}")'''

#sade ededlerin tapilmasi
'''a=int(input())
i=1
say=0
if a>1 :
    while i<=a :
        if a%i==0:
            say=say+1
        i=i+1
    if say==2 :
        print("sade")
    else:
        print("murekkeb")
else:
    print("ne sade, ne de murekkeb")'''















