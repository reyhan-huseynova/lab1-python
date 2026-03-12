'''from random import*
for j in range (1,6):
    print(f"{j}. row:", end=" ")
    for i in range (1,11):
        a=randint(1,50)
        print(a, end=" ")
    print()'''

#vurma cedveli
'''for i in range (1,11):
    for j in range (1,11):
        print(f"{i}*{j}={i*j}")'''

#ededin vurma cedvelinde olub olmamasi
'''a=int(input("insert a number: "))
flag=0
for i in range (1,11):
    for j in range (1,11):
        if a==i*j :
            flag=1
if flag==1 :
    print("the number is in the chart")
else:
    print("the number isn't in the chart")'''

#hansi vuruqlarin hasili olmasi
'''a=int(input("insert a number: "))
flag=0
for i in range (1,11):
    for j in range (1,11):
        if a==i*j :
            flag=1
            print(f"{i}*{j}")
if flag==0 :
    print("the number isn't in the chart")'''

#-1 daxil edilenedek daxil olunan ededlerin average
'''summ=0
count=0
while True :
    a=int(input())
    if a==-1 :
        break
    summ+=a
    count+=1
print(summ/count)'''

#ededin sade bolenleri
'''a=int(input())
for divident in range (2, a+1):
    count=0
    for j in range (1, divident+1):
        if divident%j==0:
            count+=1
    if count==2 and a%divident==0:
        print(divident)
        a=a//divident'''

#sade vuruqlar
'''n=int(input("insert a number:"))
factor=2
while n<=2:
    n=int(input("insert a number:"))
print("{} ededin sade vuruqlari". format(n))
i=1
while factor<=0:
    if n%factor==0:
        print(i,"->",factor)
        i+=1
        n//=factor
    else:
        factor+=1'''

#2likden 10luga
'''a=int(input())
count=0
copy=a
while a>0 :
    a//=10
    say+=1
onluq=0
for i in range (count):
    digit=copy%10
    onluq=onluq+digit*2**i
    copy=copy//10
print(onluq)'''

#10luqdan 2liye
'''eded=int(input())
power=1
binary=0
while eded>0:
    qaliq=eded%2
    binary=binary+qaliq*power
    power=power*10
    eded=eded//2
print(binary)

eded=12,6,3,1,0; binary=0,0+0*1,0+0*10,0+1*100,100+1*1000,
power=1,10,100,1000,10000, qaliq=0,0,1,1'''





