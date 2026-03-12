#random eded cixarilmasi
'''from random import*
for i in range (5):
    a=randint(1,100)
    print(f"{i}ci random eded {a}dir")'''

#5 setirde 10 random eded
'''from random import*
for i in range (1,6): #5 setir
    print(f"{i}. setir:",end=" ")
    for j in range(10): #10 tesadufi eded
        a=randint(1,100)
        print(a,end=" ") # her 10 eded yeni eyni setirde
    print() #her setri ayirdi'''
    
#bu setirlerdeki butun ededlerin cemi
'''s=0
from random import*
for i in range (1,6):
    print(f"{i}. setir:",end=" ")
    for j in range(10):
        a=randint(1,100)
        s=s+a
        print(a,end=" ")
    print()
print(s)'''

#her setirdeki ve umumi ededlerin cemi
'''k=0
from random import*
for i in range (1,6):
    s=0
    print(f"{i}. setir:",end=" ")
    for j in range(10):
        a=randint(1,100)
        s=s+a
        k=k+a
        print(a,end=" ")
    print(f"cem: {s}")
print(f"umumi cem: {k}")'''

#umumi max eded
'''from random import*
m=0
for i in range (1,6):
    print(f"{i}. setir:", end=" ")
    for j in range(10):
        a=randint(1,100)
        if a>m:
            m=a
        print(a,end=" ")
    print()
print(f"{m} max ededdir")'''

#her setirdeki max eded
'''from random import*
for i in range (1,6):
    m=0
    print(f"{i}. setir:", end=" ")
    for j in range(10):
        a=randint(1,100)
        if a>m:
            m=a
        print(a,end=" ")
    print()
    print(f"{m} max ededdir")'''

#2ci max eded
'''from random import*
for i in range (1,6):
    m1=0
    m2=0
    print(f"{i}.setir", end=" ")
    for j in range(10):
        a=randint(1,100)
        if a>m1:
            m2=m1
            m1=a
        elif a>m2 and a!=m1 :
            m2=a
        print(a,end=" ")
    print()
    print(f"{m2} 2ci, {m1} max ededdir")'''

#her siradaki minimum eded
'''from random import*
for i in range (1,6):
    m=100
    print(f"{i}. setir:", end=" ")
    for j in range(10):
        a=randint(1,100)
        if a<m:
            m=a
        print(a,end=" ")
    print()
    print(f"{m} minimum ededdir")'''






