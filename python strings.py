#stringdeki herflerin sayi
'''c=input("enter a sentence")
count=0
for i in c:
    if "a"<=i<="z" or "A"<=i<="Z":
        count+=1
print(count)'''

#stringdeki sozleri ayirir
'''s=input()
soz=""
sozler=[]
for i in range (len(s)):
    if ("a"<=s[i]<="z" or "A"<=s[i]<="Z"):
        soz+=s[i]
    elif not ("a"<=s[i]<="z" or "A"<=s[i]<="Z"):
        if len(soz)!=0:
            sozler+=[soz]
        soz=""
if len(soz) !=0:
    sozler+=[soz]
print(sozler)'''

#cumledeki reqemler cemi
'''c=input("enter a sentence: ")
s=0
for i in c: #or 'for i in range(len(s))'
    if "0"<=i<="9":
        s+=int(i)
print(s)'''

#cumledeki ededler cemi
'''s=input("enter a sentence: ")
eded=""
ededler=[]
for i in range (len(s)):
    if "0"<=s[i]<="9":
        eded+=s[i]
    elif not "0"<=s[i]<="9":
        if len(ededler)!=0:
            ededler+=[eded]
            eded=""
if len(ededler)!=0:
    ededler+=[eded]
print(ededler)'''

#teqdimat2 ex1 herflerin evezlenmesi
'''s=input("enter a sentence: ")
c=""
for i in range (len(s)):
    if s[i]=="a":
        c+="b"
    elif s[i]=="b":
        c+="a"
    elif s[i]=="A":
        c+="B"
    elif s[i]=="B":
        c+="A"
    else:
        c+=s[i]
print(c)'''

#bosluqlarin sayi ve indexi
'''def findd(x):
    count=0
    yer=[]
    for i in range (len(x)):
        if x[i]==" ":
            count+=1
            yer+=[i]
    return count, yer
s=input("enter: ")
#print(f" bosluqlarin sayi {findd(s)} ve indexleri \
#{findd(s)[1][0]} ve {findd(s)[1][1]}")
print(f" bosluqlarin sayi {findd(s)} ve indexleri \
{findd(s)[1][::]}")'''

#ad soyadin inisiallara cevrilmesi
'''s=input("enter full name: ")
name=""
names=[]
for i in range (len(s)):
    if ("a"<=s[i]<="z" or "A"<=s[i]<="Z"):
        name+=s[i]
    elif not ("a"<=s[i]<="z" or "A"<=s[i]<="Z"):
        if len(name)!=0:
            names+=[name]
        name=""
if len(name)!=0:
    names+=[name]
initials=names[-1]+" "+names[0][0]+"."+" "+names[1][0]
print(initials)'''
#funksiya vasitesile eynisi
'''def findd(x):
    for i in range (len(x)):
        if x[i]==" ":
            return i
s=input("enter full name: ")
n=findd(s) #boslugun indexi
name=s[:n]
s=s[n+1:]
n=findd(s)
f_name=s[:n]
s=s[n+1:]
n=findd(s)
surname=s[n+1:]
print(f"{surname} {name[0]} {f_name[0]}")'''
