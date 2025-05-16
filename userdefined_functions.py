#function without arguments and without return
'''
def maxx():
    n=eval(input("enter a collection:"))
    if type(n) not in (list,tuple,str):
        print(n)
    else:
        m=n[0]
        s=n[0]
        for i in n:
            if i>m:
                m=i
            if i<s:
                s=i
        print(m,s)
maxx()
'''

'''
def reverse():
    s=input('enter a sentence')
    st=s.split()
    st=st[::-1]
    for i in st:
        print(i,end=' ')
reverse()
'''

'''
def sum_of_digits():
    
    s=0
    n=int(input('enter a number:'))
    while(n>0):
        r=n%10
        s+=r
        n=n//10
    print(s)
a=sum_of_digits()
'''

'''
def factorial():
    fact=1
    n=int(input('enter a number'))
    for i in range(n,0,-1):
        fact*=i
    print(fact)
factorial()
'''

'''
def prime():
    n=int(input('enter a number'))
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    if c==0:
        print('prime')
    else:
        print('not a prime')
prime()
'''

'''
def prime_in_range():
    n=int(input('enter the range'))
    c=0
    if n>3:
        print(2,3,end=' ')
        for i in range(4,n+1):
              for j in range(2,(i//2)+1):
                    if i%j==0:
                        c+=1
              if c==0:
                  print(i,end=' ')
              c=0
prime_in_range()
'''

'''
def perfectno():
    n=int(input('enter a no:'))
    f=0
    for i in range(1,n):
        if n%i==0:
            f+=i
    if n==f:
        print('perfect no')
    else:
        print('not a perfect no')
perfectno()
'''

'''
def perfectnos_in_range():
    n=int(input('enter the range:'))
    f=0
    for i in range(2,n+1):
        for j in range(1,(i//2)+1):
            if i%j==0:
                f+=j
        if i==f:
            print(f,end=' ')
        f=0
perfectnos_in_range()
'''

'''
def armstrong():
    n=int(input('enter a number:'))
    t=n
    s=0
    l=len(str(n))
    while n>0:
        r=n%10
        s=s+(r**l)
        n=n//10
    if s==t:
        print('armstrong')
    else:
        print('not')
armstrong()
'''

'''
def armstrongno_in_range():
    n=int(input('enter the range:'))
    for i in range(1,n+1):
        t=i
        s=0
        l=len(str(i))
        while i>0:
            r=i%10
            s+=(r**l)
            i=i//10
        if s==t:
            print(t,end=' ')
armstrongno_in_range()
'''


#function with arguments and without return
'''
#k=10,21,2,89,1
def maxx(n):
    if type(n) not in (list,tuple,str):
        print(n)
    else:
        m=n[0]
        s=n[0]
        for i in n:
            if i>m:
                m=i
            if i<s:
                s=i
        print(f'max ={m},min ={s}')
#maxx(k)
maxx(eval(input('enter a collection')))
'''

'''
def reverse(s):
    s=s.split()
    st=s[::-1]
    for i in st:
        print(i,end=' ')
reverse(input('enter a sentence'))
'''

'''
def sodigits(n):
    s=0
    while(n>0):
        r=n%10
        s+=r
        n=n//10
    print(s)
    
sodigits(int(input('enter a number:')))
'''

'''
def facto(n):
    f=1
    for i in range(n,1,-1):
        f*=i
    print(f)
    
facto(int(input('enter a number:')))
'''

'''
def primeno(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    if c==0:
        print('prime no')
    else:
        print('not a prime')
primeno(int(input('enter a number:')))
'''

'''
def primenos(n):
    for i in range(2,n+1):
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1
        if c==0:
            print(i,end=' ')
primenos(int(input('enter a range:')))
'''

'''
def perfectno(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if n==s:
        print('perfect no')
    else:
        print('not a perfect no')
perfectno(int(input('enter a no')))
'''

'''
def perfectnos(n):
    for i in range(1,n):
        s=0
        for j in range(1,i):
            if i%j==0:
                s+=j
        if i==s:
            print(i,end=' ')
    
perfectnos(int(input('enter the range')))
'''

'''
def armstrongno(n):
    t=n
    s=0
    l=len(str(n))
    while n>0:
          r=n%10
          s+=(r**l)
          n=n//10
    if t==s:
          print('armstrong no')
    else:
          print('not a armstrong no')
armstrongno(int(input('enter a no')))
'''

'''
def armstrongnos(n):
    for i in range(1,n):
        t=i
        s=0
        l=len(str(i))
        while i>0:
            r=i%10
            s+=(r**l)
            i=i//10
        if s==t:
            print(t,end=' ')
armstrongnos(int(input('enter the range')))
'''

'''
#type 3 function without arg and with return
def prime():
    n=100
    out=[]
    for i in range(1,n,2):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            out.append(i)
    return out,'hai'
print(prime()) in type 3 function call has to be printed else no out when simply calling it
#prime() #no output
'''


'''
def operation():
    a=30
    b=40
    return a+b,a-b,a*b,a/b,a//b
print(operation())
'''
'''
def e_repeated():
    s=input('enter a string collection')
    o=''
    i=0
    while (s[i] in s) and (s[i] not in o):
        o+=s[i]
        i+=1
        if i==len(s):
            break
    return tuple(o)
print(e_repeated())
'''
'''
def repeat():
    inp='abaababcdef'
    o=()
    for i in inp:
        if i not in o:
            o+=(i,)
    return o
print(repeat())
'''

'''
def u_char():
    inp='abababcdef'
    out=()
    for i in inp:
        c=0
        for j in inp:
            if i==j:
                c+=1
        if c==1:
            out+=(i,)
    return out
print(u_char())
'''

'''
l=[1,2,4,2,20,32]
k=20
for i in l:
    if i==k:
        print(l.index(i))
'''


#21/2/2025
#basic arithmatic operation

'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    return 'zeroDivision error'
def mod(a,b):
    return a%b

a=int(input('enter a number'))
b=int(input('enter a number'))
op=input('enter an operator (+,-,*,/,%) to perform arithmetic opration')
if op=='+':
    print(add(a,b))
elif op=='-':
    print(sub(a,b))
elif op=='*':
    print(mul(a,b))
elif op=='/':
    print(div(a,b))
elif op=='%':
    print(mod(a,b))
else:
    print('invalid operator')
'''

'''counting the no of currency needed'''
'''
n=28768

def notes(n):
        d={}
        c=[2000,500,200,100,50,20,10,5,2,1]
        for i in c:
            d[i]=n//i
            n=n%i
            
                if n//i!=0:
                c=n//i
                d[i]=c
                n=n-(c*i)
            
        return d
print(notes(n))   
'''

'''
def mising_no(a,b):
    for i in range(1,b+1):
        if i not in a:
            return i
print(mising_no([1,2,3],4))
'''

'''
#22/5/2025    nested function
def outer():
    a=10
    b=20
    print(a+b)
    def inner():
        p='hai'
        q='hello'
        print(p+q)
        def inner1():
            r=[1,2,3,4,5,6]
            print(r[::-1])
        inner1()
    inner()
   #inner()

outer()
'''

#24/2/2025

'''
def a(a,*b):
    print(a)
    print(b)
a(1)
'''
#packing
'''
def pack(*a):
    for i in a:
        for j in i:
            if type(j)==int:
                facto=1
                for k in range(j,0,-1):
                    facto*=k
                print(j,facto)
            elif type(j)==str:
                print(j,j[::-1])
            else:
                print(j)

pack([1,5,7,'hai'],[8,9,'hello',[2,3]],[(1,2),3,4,7,'python'])

'''

'''
#unpacking      25/2/2025
#tuple unpacking
def unpach(a,b,c):
    print(a,b,c)
unpack(*'hai')
'''

'''
inp=[[1,2,3],[4,5,6],[7,8,9],'hai',3]
#expected_out=[1, 2, 3, 4, 5, 6, 7, 8, 9, 'hai', 3]
out=[]
for i in inp:
    if type(i)==list:
        for j in i:
            out.append(j)
    else:
        out.append(i)
print(out)
'''
inp=[[1,2,3],[4,5,6],[7,8,9],'hai',3]

out=[]
for i in inp:
    if type(i)==list:
        for j in i:
            out.append(j)
    else:
        out.append(i)
print(out)






        
