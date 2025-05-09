#1.waptp all the integers present in a list
'''
a=[1,2,3,2.2,'9238',1+2j,[23],29,(23,32),32]
for i in range(len(a)):
    if type(a[i])==int:
        print(a[i],end=' ')
'''

#2.wapt find the length of homogenous tuple without len().
'''
a=(2,3,5,3,75,82,23.23)
c=0
for i in range(len(a)):
    if i==0:
        c+=1
    elif type(a[i])!=type(a[i-1]):
        print('condition violated so, heterogenous tuple')
        break
    c+=1
else:
    print('homogenous')
    print('length =',c)
'''

#3.wapt extract all the even numbers present in a list
'''
a=[32,89421,827,9287,234,123532,8,20]
for i in range(len(a)):
    if a[i]%2==0:
        print(a[i],end=' ')
'''

#4.wapt remove dublicates from list
'''
a=[32,89421,827,32,8,234,9287,234,123532,8,20]
out=[]
u=set(a)
i=0
while i<len(a):
    if a[i] in u:
        out.append(a[i])
        u.remove(a[i])
    i+=1
print(out)
'''

#5.wap to reverse a string without using slicing
'''
s='abcdef'
out=''
for i in range(len(s)-1,0-1,-1):
    out+=s[i]
print(out)
'''
#another method
'''
for i in range(len(s)):
    out=s[i]+out
print(out)
'''

#6.wapt extract all the lowercase characters in a string only if the ascii value
#is even
'''
s='agfgdfsALKJkljhgh'
for i in range(len(s)):
    if 'a'<=s[i]<='z' and ord(s[i])%2==0:
        print(s[i],end='',sep='')
'''

#7.waptc whether the last digit of an integer is even or not
'''
a=str(122)
for i in range(len(a)-1,len(a)):
    if int(a[i])%2==0:
        print('even')
    else:
        print('odd')
'''

#8.wapt extract all the key value pars from  the dictionary only if the keys are
#of string datatype and values are integers
'''
a={'fd1':233333,'fd2':8976,'lk':981,12:'kjjj',(234,98):1.3}
for keys,values in a.items():
    if type(keys)==str and type(values)==int:
        print(keys,values)
'''


#9.wapt extract key value pars from the dictionary only if both keys and values are exactly same
'''
a={'12':'12','gh':'gh','hi':23,'hello':'hi','hey':'hey'}
for keys,values in a.items():
    if keys==values:
        print(keys,values)
'''

#10.wapt get the following output using len function
'''
s='power star'
ex_out={'power':5,'star':4}
out={}
s=s.split()
for i in s:
    out[i]=len(i)
print(out)
'''

#11.wapt get the following output
'''
s='power star'
ex_out={'power':'rewop','star':'star'}
out={}
s=s.split()
for i in s:
    out[i]=i[::-1]
print(out)
'''

#12.wapt extract all the non default values from a list.
a=[1,98,3.2,0,0j,0+0j,0-0j,0.0000,29,0.32]
'''
for i in a:
    if bool(i):
        print(i,end=' ')
#pascals triangle
'''

#13.waptc whether the list is homogenous or not
'''
a=[1,2,3,2]
if len(a)==1:
    print('homogenous')
else:
    t=type(a[0])
    for i in range(len(a)):
        if type(a[i])!=t:
            print('non homogenous')
            break
    else:
        print('homogenous')
'''

#14.wapt replace the space by * present in a string
'''
s='abc defgh 123jo !@#hok  '
out=''
for i in s:
    if i==' ':
        out+='*'
    else:
        out+=i
print(out)
'''

#15.wapt count the no of occurrence of a specified character.
'''
s='abc defgh 123jo !@#hok  adsfkjlkjj'
b='j'
out={}
for i in s:
    if i==' ':
        pass
    elif i not in out:
        out[i]=1
    else:
        out[i]=out[i]+1
print(out[b])
'''

#16.wapt get the following output
'''
s='always keep smiling'
ex_out='syawla peek gnilims'
s=s.split()
out=''
for i in s:
    out+=(i[::-1]+' ')
print(out)
'''
'''
s='always keep smiling'
s=s.split()
out=[]
for i in s:
    out.append(i[::-1])
for j in out:
    print(j,end=' ')
'''

#17.wap to get the following output
'''
inp='push maadi kushi padi'
ex_out={'push':'ph','maadi':'a','kushi':'s','padi':'pi'}
inp=inp.split()
out={}
for i in inp:
    k=inp.index(i)
    if len(i)%2==0:
        out[i]=inp[k][0]+inp[k][-1]
    else:
        m=len(i)//2
        out[i]=inp[k][m]
print(out)
'''

#18.wapt toggle a string.
'''
s='skjdhAJHkjkhAJKLJ@#$%123tskjSJkj'
ex_out='SKJDHajhKJKHajklj@#$%123TSKJsjKJ'
out=''
for i in s:
    if 'A'<=i<='Z':
        out+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=i
print(out)
'''

#19.wap to extract upper,lower,digit and special characters present in a string
#to different output variables
'''
s='skjdhAJHkjkhAJKLJ@#$%123tskjSJkj'
lowercase=''
Uppercase=''
numbers=''
spl_chars=''
out={}
for i in s:
    if 'A'<=i<='Z':
        Uppercase+=i
    elif 'a'<=i<='z':
        lowercase+=i
    elif '0'<=i<='9':
        numbers+=i
    else:
        spl_chars+=i
out={'Uppercase':Uppercase,'lowercase':lowercase,'numbers':numbers,'spl_chars':spl_chars}
print(out)
'''

#20.waptg the following output
'''
s='hai hello'
ex_out={'hai':'ai','hello':'eo'}
out={}
s=s.split()
for i in s:
    t=''
    for j in range(len(i)):
        if i[j] in 'aeiouAEIOU':
            t+=i[j]
        out[i]=t
print(out)
'''

#21.wapt get the following output
'''
s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
ex_out=['com', 'py', 'html', 'com', 'org']
out=[]
for i in range(len(s)):
    k=0
    k=s[i].find('.')
    out.append(s[i][k+1::])
print(out)
'''

'''
#22.wapt get the following output.
s=['jiocinema.com','file.py','web.html','amazon.com','www.org']
{'com': ['jiocinema', 'amazon'], 'py': ['file'], 'html': ['web'], 'org': ['www']}
out={}
for i in range(len(s)):
    k=0
    k=s[i].find('.')
    if s[i][k+1:] not in out:
        t=[]
        out[s[i][k+1:]]=t
        c=s[i][:k]
        out[s[i][k+1:]].append(c)
    else:
        c=s[i][:k]
        out[s[i][k+1:]].append(c)
print(out)
'''

'''
#23.wapt get the following output
L=['hai',34,3.4,'hello',90,'byebye']
ex_out={'hai': 'hi', 'hello': 'ho', 'byebye': 'be'}
out={}
for i in L:
    if type(i)==str:
        out[i]=i[0]+i[-1]
print(out)
'''

#24.wapt get the following output
'''
inp='hello'
ex_out={}
out={}
for i in range(len(inp)):
    out[i]=inp[i]
print(out)
'''

#25.wapt extract all the string values present in list only
#if the string is palindrome
'''
L=['hai',34,3.4,'helleh',90,'byeyb']
for i in L:
    if isinstance(i,str):
        if i==i[::-1]:
            print(i,end=' ')
'''

#26.wapt return the positions of vowels present in the given string.
'''
s='sakjjAJalkj'
for i in range(len(s)):
    if s[i] in 'aeiouAEIOU':
        print(s[i],'at position',i)
'''

#27.waptc whether the given collection is having nested collection or not.
'''
L=['hai',34,3.4,'helleh',90,'byeyb',[1,2]]
for i in L:
    if isinstance(i,list) or isinstance(i,tuple) or isinstance(i,set) or isinstance(i,dict):
        print('has nested collection')
        break
else:
    print('not ')
'''

#28.wapt count the no of words in a string
'''
s='hi hello how are you'
s=s.split()
c=0
for i in s:
    c+=1
print(c)
'''

#29.waptc wether the no is neon no or not
'''
n=9
t=n
s=n**2
sum=0
for i in str(s):
    sum+=int(i)
if sum==t:
    print(t,'neon number')
else:
    print(t,' is not a neon number')
'''

#30.wapt find the longest word in a string.
'''
s='hi hello how are you'
l=0
s=s.split()
for i in s:
    if len(i)>l:
        l=len(i)
        t=i 
print(t)
'''

#31.waptreplace the special char present in a string by space.
'''
s='hi&hello*how&are&you'
ex_out='hi hello how are you'
out=''
for i in s:
    if 'a'<=i<='z' or 'A'<=i<='Z' or '0'<=i<='9':
        out+=i
    else:
        out+=' '
print(out)
'''

#32.waptp the square of all the integers present in a list.
'''
L=['hai',34,3.4,'helleh',90,'byeyb',[1,2]]
for i in L:
    if isinstance(i,int):
        print(i,'--->',i**2)
'''

#33.wapt extract all the odd numbers present at even index from a list.
'''
L=[0,1,2,3,32,123,2,534,23,23,987]
for i in range(len(L)):
    if i%2==0  and L[i]%2!=0:
        print(L[i])
'''



'''
n=7
out=[]
for i in range(n):
    t=[]
    for j in range(i+1):
        if j==0 or j==i:
            t.append(1)
        else:
            t.append(out[i-1][j-1] + out[i-1][j])
    out.append(t)
    #print(out[-1])
k=len(out)
for i in out:
    print('  '*k,end='')
    for j in i:
        print(j,end='   ')
    k-=1
    print()
'''



