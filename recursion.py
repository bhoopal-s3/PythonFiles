'''
def permut(a,i=0):
    if i==len(a):
        print(a)
    for j in range(i,len(a)):
        w=[]
        for c in a:
            w.append(c)
        w[i],w[j]=w[j],w[i]
        permut(w,i+1)
permut('abc')
'''
#26/2/2025
#factorial
'''
def fact(n):
    if n==0:
        return 1
    return n * fact(n-1)
    print(n)
print(fact(5))
'''

#5432112345   

'''
def seq(n):
    if n==0:
        return
    print(n,end=' ')
    seq(n-1)
    print(n,end=' ')
seq(5)
'''

#27/2/2025
'''
def conv(inp,i=0,out=''):
    if i>=len(inp):
        return out
    if 'A' <= inp[i] <= 'Z':
        out+=inp[i].lower()
    elif 'a' <= inp[i] <= 'z':
        out+=inp[i].upper()
    return conv(inp,i+1,out)
print(conv('AbcdDedFGhI'))
'''

#28/2/2025
'''
n=10
i=1
while i<n*2:
    print(i,end=' ')
    i+=2
'''
#printing n number of odd numbers
'''
def odd(n,i=1):
    if i>n*2:
        return print()
    print(i,end=' ')
    return odd(n,i+2)
odd(10)
'''

#printing n number of even numbers
'''
def even(n,i=2):
    if i>=n*2+2:
        return print()
    print(i,end=' ')
    return even(n,i+2)
even(10)
'''





'''
n=12323
out=''
while n>0:
    r=n%10
    out=out+str(r)
    n=n//10
print(out)
'''
#wa recursive program to reverse a number
'''
def rev(n,out=''):
    if n<=0:
        return out
    r=n%10
    out=out+str(r)
    n=n//10
    return rev(n,out)
print(rev(12342))
'''

#wa recursive program to sum the digits
'''
def summ(n,out=0):
    if n<=0:
        return out
    r=n%10
    out+=r
    n=n//10
    return summ(n,out)
print(summ(12345))
'''

#fibonacci
'''
n=10
f=0
s=1
if n==1:
    print(f)
elif n==2:
    print(f,s)
else:
    i=3
    print(f,s,end=' ')
    while i<=n:
        t=f+s
        f=s
        s=t
        print(t,end=' ')
        i+=1
'''       

#wa recursion program to find the n number of  fibonacci series
'''
f=0
s=1
def fib(m):
    if m<=0:
        return
    elif m==1:
        return print(f)
    elif m==2:
        return print(f,s)
    else:
        print(f,s,end=' ')
        def fibo(m,i=3):
            global f,s
            if i>m:
                return
            t=f+s
            f=s
            s=t
            print(t,end=' ')
            return fibo(m,i+1)
        fibo(m)
fib(10)
'''     

'''
sen='hi hello how are you'
sen=sen.split()
i=0
l=len(sen)
while i<l:
    print(sen[-(i+1)],sep=' ',end=' ')
    i+=1
''' 
    
#reverse the words in the sentence
'''
sen='hi hello how are you'
def reverse(s,i=1):
    l=len(s)
    if i>l:
        return 
    print(s[-i],sep=' ',end=' ')
    return reverse(s,i+1)
reverse(s=sen.split())
'''

'''
def pat(n,s=ord('A'),i=0,j=0):
    if i>=n:
        return
    while j<i+1:
        print(chr(s),end=' ')
        j+=1
        s+=1
    print()
    return pat(n,s,i+1,j=0)
pat(6)
'''
'''
A 
B C 
D E F 
G H I J 
K L M N O 
P Q R S T U 
'''
'''
def pat(n,s=ord('A'),i=0,j=0):
    if i>=n:
        return
    while j<i+1:
        print(chr(s),end=' ')
        j+=1
        s+=1
        if s>ord('Z'):
            s=ord('A')
    print()
    return pat(n,s,i+1,j=0)
pat(10)
'''
'''
A 
B C 
D E F 
G H I J 
K L M N O 
P Q R S T U 
V W X Y Z A B 
C D E F G H I J 
K L M N O P Q R S 
T U V W X Y Z A B C
'''
'''
def pat(n,s=ord('0'),i=1,j=0):
    if i>=n+1:
        return
    if i%2==1:
        s=ord('1')
        print(chr(s),end=' ')
    else:
        s=ord('0')
        print(chr(s),end=' ')
    while j<i-1:
        print(chr(s),end=' ')
        j+=1
        s+=1
    print()
    return pat(n,s,i+1,j=0)
pat(10)
'''

#3/3/2025
#permutation and combination
'''
def permut(a,i=0):
    if i==len(a):
        print(a)
    for j in range(i,len(a)):
        w=[]
        for c in a:
            w.append(c)
        w[i],w[j]=w[j],w[i]
        permut(w,i+1)
permut('abc')
'''

'''
def perm(a,i=0):
    if i==len(a):
        print(a)
    for j in range(i,len(a)):
        w=list(a)
        w[i],w[j]=w[j],w[i]
        perm(w,i+1)
perm('abcd')
'''
'''
print('/n/n')
from itertools import permutations,combinations
print(list(permutations('abc')))

print(list(combinations('abc',3)))
'''

#waptc strong number or not 145 1!+4!+5!=145
'''
i=0
s=0
c=n=145
while n>0:
    r=n%10
    f=1
    for i in range(1,r+1):
        f*=i
    s+=f
    n=n//10
if c==s:
    print(c,'strong no')
else:
    print(c,'no')
'''

#happy numbers
'''
19
1^2 + 9^2= 1+81= 82
8^2 + 2^2 = 64+4 = 68
6^2 + 8^2 =36+64 = 100
1^2 + 0^2 +0^2=1 so 19 is happy number

'''
'''
n=19
s=0
su=0
def happy(n):
    global s,su
    while n>0:
        r=n%10
        f=0
        s+=r**2
        n=n//10  
happy(n)
 '''

#Happy number
'''
def happy(a,out=0):
    global temp
    temp=0
    for i in a:
        out+=int(i)**2
    temp=out
    if not 1<=temp<=9:
        happy(str(temp),out=0)
    else:
        temp=temp
happy(input('enter the number:'))
if temp==1:
    print('happy number')
else:
    print('unhappy number')
'''


#Define a function which will work similar to slicing

inp='programming'
s=0
e=len(inp)
st=2
i=0
out=''
'''
while i<e and i<len(inp):
    out+=inp[i]
    i+=st
print(out)
'''
'''
def slice(inp,s,e,st=1,i=0,out=''):
    if i>=e and i>=len(inp):
        return out
    if i>s:
        out+=inp[i]
    return slice(inp,st+s,e,i+st,st,out)
slice(inp,s,e,st)
'''
    
