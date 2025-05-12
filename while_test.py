'''
#a=1234567
a=8735246
odd=0
even=0
while a:
    r=a%10
    if r%2==0:
        even+=r
    else:
        odd+=r
    a=a//10
print(even)
print(odd)
'''

'''
s='python**fina*l'
ex_out='pythfinl'
s='erase*****'
op=''
i=0
out=''
while i<len(s):
    if s[i]=='*':
        l=len(out)
        out=out[:l-1]
    else:
        out+=s[i]
    i+=1
print(out)
'''

'''
s=5
op=[5,16,8,4,2,1]
out=[]
out.append(s)
while s!=1:
    if s%2!=0:
        s=s*3+1
        out.append(s)
    else:
        s=s//2
        out.append(s)
print(out)
'''

#remove the repeated values in the dictionary
'''
a={'a':1,'b':2,'c':1,'d':3,'e':2}
ex_op={'a':1,'b':2,'d':3}
out={}
k=list(a)
v=set(a.values())
i=0
while i<len(k):
    if a[k[i]] in v:
        out[k[i]]=a[k[i]]
        v.remove(a[k[i]])
    i+=1
print(out)
'''

#waptp the pattern
'''
A 
B C 
D E F 
G H I J 
K L M N O 
'''
'''
s=ord('A')
i=0
n=5
while i<n:
    j=0
    while j<i+1:
        print(chr(s),end=' ')
        s+=1
        j+=1
    i+=1
    print()
'''

n=6
i=1
k=n
while i<n*2:
    if i%2==1:
        print((k//2+2)*' '+i*'*')
    i+=1
    k-=1

k=n
i=1
m=n*2-2
while m>0:
    if m%2==1:
        print((i//2*' ')+m*'*')
    m-=1
    i+=1
