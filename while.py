#1.WAPTP THE FOLLOWING USING WHILE LOOP
#A. 1ST 10 EVEN NOS
#B. 1ST 10 ODD NOS
#C. 1ST 10 NATURAL NOS
#D. 1ST 10 WHOLE NOS
'''
n=10
i=2
while i<=n*2:
    print(i,end=' ')
    i+=2
print()

i=1
while i<=n*2:
    print(i,end=' ')
    i+=2
print()
i=1
while i<=n:
    print(i,end=' ')
    i+=1
print()
i=0
while i<=n-1:
    print(i,end=' ')
    i+=1
print()
'''


#2.waptp 1st 10 int and their squares using while loop
'''
n=10
i=1
while i<=n:
    print(i,'\t',i**2)
    i+=1
'''

#3.waptp 10,20,30,......,300
'''
n=300
i=10
while i<=300:
    print(i,end=',')
    i+=10
'''
#4.waptp 105,98,91 ... ... ...7
'''
i=105
n=7
while i>n:
    print(i,end=',')
    i-=7
else:
    if i==7:
        print(i)
'''
#5.waptp first 10 natural no in reverse order using while loop
'''
i=10
n=1
while i>=n:
    print(i)
    i-=1
'''

#6.waptp sum of 10 natural nos
'''
i=1
n=10
su=0
while i<=n:
    su=su+i
    i+=1
print(su)
'''

#7.waptp sum of 1st 10 even nos
'''
i=2
n=10
su=0
while i<=n*2:
    su+=i
    i+=2
print(su)
'''

#8.waptp table of a number entered from the user
'''
n=int(input('enter a no:'))
i=1
l=10
while i<=l:
    print(n,'x',i,'=',n*i)
    i+=1
'''
#9.waptp all even nos that falls between 2 nos (exclusive of both nos) entered
# from the user using while loop
'''
fst=int(input('enter 1st no'))
sec=int(input('enter 2nd no'))
if fst>sec:
    greatest=fst
    smallest=sec
else:
    smallest=fst
    greatest=sec
if smallest%2==0:
    smallest+=1
while smallest<greatest:
    if smallest%2==0:
        print(smallest)
    smallest+=1
'''

#10.waptc whether a no is prime or not using while loop
'''
n=int(input('enter a no'))
i=2
k=0
if n<0:
    print('enter +ve no')
elif n==0 or n==1:
    print('not a prime')
else:
    while i<n:
        if i!=n and n%i==0:
            k+=1
        i+=1
    if k==0:
        print('prime')
    else:
        print('not')
'''

#11.waptf the sum of the digits of a no accepted from the user
'''
n=int(input('enter a no'))
r=0
s=0
while (n!=0):
    r=n%10
    s+=r
    n=n//10
print(s)
'''

#12.waptf the product of the digits of a no accepted from the user
'''
n=int(input('enter a no'))
r=0
p=1
if n==0:
    p=0
while (n!=0):
    r=n%10
    p=p*r
    n=n//10
print(p)
'''

#13.wapt reverse the num accepted from user using while loop
'''
n=int(input('enter a no'))
r=0
rev=''
while (n!=0):
    r=n%10
    rev=rev+str(r)
    n=n//10
int(rev)
print(rev)
'''
'''
n=123
rev=0
while n!=0:
    rev=rev*10+n%10
    n//=10
print(rev)
'''
#14.waptd the no names of the digits of a no entered by user,for example if
#the no is 231 then output should be Two Three One
'''
n=int(input('enter a no'))
d={0:'Zero ',1:'One ',2:'Two ',3:'Three ',4:'Four ',5:'Five ',6:'Six ',7:'Seven ',8:'Eight ',9:'Nine '}
r=0
st=''
if n==0:
    st=d[0]
else:
    while (n!=0):
        r=n%10
        st=d[r]+st
        n=n//10
print(st)
'''

#15.waptp the fibonacci series till n terms using while loop
'''
n=int(input('enter a no:'))
if n==1:
    print(1)
elif n==2:
    print(1,1,sep=' ',end=' ')
elif n==0:
    print('enter +ve no')
else:
    i=3
    ft=1
    st=1
    print(ft,st,sep=' ',end=' ')
    while i<=n:
        nt=ft+st
        ft=st
        st=nt
        print(nt,end=' ')
        i+=1
'''

#16.waptp the factorial of a no accepted from user.
'''
n=int(input('enter a no:'))
c=n
fact=1
while c>1:
    fact=c*fact
    c-=1
print(fact)
'''

#17.waptc whether a no is armstrong or not (armstrong no is a no that is equal
#to the sum of cubes of its digts for example:153 = 1^3 + 5^3 + 3^3
'''
n=int(input('enter a no:'))
a=len(str(n))
d=n
o=0
while d>0:
    r=d%10
    o=o+(r**a)
    d=d//10
    
if o==n:
    print('yes')
else:
    print('no')
'''
#18.generate a series of armstrong no's till user specified value
# if inp=1000,    exp_out=1 2 3 4 5 6 7 8 9 153 370 371 407 
'''
n=int(input('enter a no:'))
c=1
o=0
while c<=n:
    a=len(str(c)) 
    d=c
    while d>0:
        r=d%10
        o=o+(r**a)
        d=d//10
    if o==c:
        print(c,end=' ')
    c+=1
    o=0
'''

#19.wapt add first n terms of the following series using while loop
#1/1! + 1/2! +1/3!+ ..... + 1/n!
'''
n=int(input('enter a number'))
s=0
fact=1
i=1
while(i<=n):
    fact=fact*i
    s+=1/fact
    i+=1
print(s)
'''
#20.wapt enter the no till the user wants and at the end it should display the sum
#of all the no's entered
'''
n=int(input('enter how many number of inputs: '))
i=1
sum=0
while i<=n:
    s=int(input(f'enter input no {i}: '))
    sum+=s
    i+=1
print(sum)
'''

#21.wapt enter the no's till the user enters zero & at the end it should display
#the count of +ve and -ve no's entered
'''
neg=0
pos=0
while 1:
    n=int(input('enter the no'))
    if n<0:
        neg+=1
    elif n>0:
        pos+=1
    else:
        break
print("positive no's count",pos)
print("negative no's count",neg)
'''

#22.waptf the HCF of two no's entered from the user
'''
n=int(input('enter a no'))
m=int(input('enter a no'))
if n>m:
    g=n
else:
    g=m
i=1
h=1
while i<=(g//2):
    if (n%i==0 and m%i==0):
        h=i
    i+=1
print(h)
'''
'''
#23.waptc decimal to binary conversion
n=int(input('enter a number:'))
out=''
if n==0:
    out=0
else:
    while n:
        b=n%2
        out=str(b)+out
        n=n//2
print(int(out))
'''

'''
#24.waptc binary to decimal
b=101
i=0
out=0
while b>0:
    n=b%2
    if n!=0:
        out+=2**i
    b=b//10
    i+=1
print(out)
'''

#25.wap to sum the sequence:
#1+1/1!+1/2!+.........+1/n!
'''
n=5
s=1
i=1
fact=1
while i<=n:
    fact=fact*i
    s+=(1/fact)
    i+=1
print(s)

'''
#26.wapt accept 10 numbers from the user & display it's average
'''
n=10
s=0
i=1
while i<=n:
    inp=int(input('enter a number'))
    s+=inp
    i+=1
print('avg is',s/10)
'''

#27.wap to accept 10 no from the user and display the largest and smallest no
'''
l=0
s=0
n=10
i=1
while i<=10:
    inp=int(input('enter a number:'))
    if inp>l:
        l=inp
    if inp<s:
        s=inp
    i+=1
print('largest is',l,'smallest is',s)
'''

#28.waptd sum of odd numbers and even numbers separately that fall between two numbers accepted from the
#user(including both numbers) using while loop
'''
even=0
odd=0
s=int(input('enter a number'))
l=int(input('enter a number'))
if s>l:
    s=l
    l=s
while s<=l:
    if s%2==0:
        even+=s
    else:
        odd+=s
    s+=1
print('sum of even numbers in the given range is',even)
print('sum of odd numbers in the given range is',odd)
'''

#29.waptd all the numbers which are divisible by 13 but not by 3 between
#100 and 500.(exclusive both numbers)
'''
n=101
while 100<n<500:
    if n%13==0 and n%3==1:
        print(n)
    n+=1
'''

#30.waptp the following series till n terms
#2,22,222,2222,22222,........n
'''
n=int(input('enter a number:'))
s=''
i=0
while i<=n-1:
    s+='2'
    if i==n-1:
        print(s,end=' ')
        break
    print(s,end=',')
    i+=1
'''
'''
n=int(input('enter a number:'))
s='2'
i=0
while i<n:
    print(s,end=',')
    s+='2'
    i+=1
'''

#31.wap the following series till n terms
'''
n=int(input('enter a number'))
i=0
while i<=n-1:
    i+=1
    print(i**2,end=' ')
'''

#32.waptf the sum of the following series(accet values of x and n from user)
#1+x/1!+x^2/2!+......x^n/n!
'''
x=int(input('enter the value of x:'))
n=int(input('enter the value of n:'))
i=0
s=1
fact=1
while i<n-1:
    i+=1
    fact=fact*i
    s+=((x**i)/fact)
print(s)
'''

#33.waptf the sum of following series:
#x+x^2/2+........x^n/n
'''
x=int(input('enter x value'))
n=int(input('enter n value'))
s=x
if n>=2:
    i=2
    while i<=n:
        s+=x**i/i
        i+=1
print(s)
'''

#34.waptf the sum of following series
#1+8+27........n terms
'''
n=int(input('enter a number'))
s=0
i=1
while i<=n:
    s+=i**3
    i+=1
print(s)
'''

#35.waptf sum of following series:
#1+2+6+24+120......n
'''
n=10
i=1
s=0
pr=1
while i<=n:
    pr=pr*i
    if i==n:
        print(pr,end=' ')
    else:
        print(pr,end='+')
    s=s+pr
    i+=1
print('=',s)
'''

#36.waptf the sum of following series:
#s=1+4-9+16-25+36-......n terms
'''
n=6
s=1
i=2
print(s,end=' ')
while i<=n:
    if i%2==0:
        pr=i**2
        print('+',pr,end=' ')
        s+=pr
    else:
        pr=i**2
        print('-',pr,end=' ')
        s-=pr
    i+=1
print('=',s)
'''

#37.wapt print all the characters in the string python using while loop.
'''
s='PYTHON'
C=0
l=len(s)
while C<l:
    print(s[C])
    C+=1
'''

#38.waptp all the factors of a number using while loop
'''
n=6
c=n
fact=1
while c>0:
    fact*=c
    c-=1
print(fact)
'''

#39.wap to get the following output
'''
1----49
2----48
3----47
.
.
.
48----2
49----1
'''

'''
n=50
t=n
i=1
while (n-1)>0 and i<t:
    print(f'{i}----{n-1}')
    n-=1
    i+=1
'''

#40.wapt extract all the upper case character from the given string
'''
s=input('enter the string:')
l=len(s)
i=0
while i<l:
    if s[i].isupper():
       print(s[i],end=' ')
    i+=1
'''

#41.wap to seperate positive and negative no from a list
'''
x=eval(input('enter the list:'))
l=len(x)
i=0
positive=[]
negative=[]
while i<l:
    if type(x[i]) in (int,float,bool): 
        if x[i]>0:
            positive.append(x[i])
        elif x[i]<0:
            negative.append(x[i])
    i+=1
print('+ve no are',positive)
print('-ve no are',negative)
'''

#42.wap that appends the type of elements from a list.
'''
n=[23,'python',23.98]
out=[]
l=len(n)
i=0
while i<l:
    out.append(type(n[i]))
    i+=1
print(out)
'''

#43.wapt fetch only even values from a dictionary.
'''
dic={'val':10,'val2':20,'val3':23,'val4':22}
l=len(dic)
i=0
k=list(dic.items())
out={}
while i<l:
    if k[i][1]%2==0:
        out[k[i][0]]=(k[i][1])
        #print(k[i][0],',',k[i][1])
    i+=1
print(out)
'''

#44.wapt extract all the string data items from the given list only if
#string is palindrome
'''
lst=['hi','hellolleh','main','naine','seves']
i=0
while i<len(lst):
    if type(lst[i])==str:
        if lst[i]==lst[i][::-1]:
            print(lst[i])
    i+=1
'''

#45.wapt extract all the upper case character, lowercase character,numbers and special
#characters into four different output variables from the given string
'''
string='aAbcdEFgh1!23#$ 32*&'
i=0
upper=''
lower=''
number=''
spl=''
while i<len(string):
    if 'A'<=string[i] <='Z':
        upper+=string[i]
    elif 'a' <= string[i] <='z':
        lower+=string[i]
    elif '0' <= string[i] <= '9':
        number+=string[i]
    else:
        spl+=string[i]
    i+=1
print(f'upper case chars are {upper}')
print(f'lower case chars are {lower}')
print(f'numbers are {number}')
print(f'spl chars are {spl}')
'''

#46.wapt get the following output

#47.wapt convert all the lowercase char to upper case chars present in
#a given string
'''
s='1213adfvaBDCS#@#&*bac'
i=0
out=''
while i<len(s):
    if 'A' <= s[i] <='Z':
        out+=chr(ord(s[i])+32)
    elif 'a' <= s[i] <= 'z':
        out+=chr(ord(s[i])-32)
    else:
        out+=s[i]
    i+=1
print(s)
print(out)
'''

#48.wapt extract all the lower case character from the given string only if its
#ascii value is even
'''
s='adfsccvstre'
ascii_even=''
i=0
while i<len(s):
    if 'a' <= s[i] <= 'z':
        if ord(s[i])%2==0:
            ascii_even+=s[i]
    i+=1
print(ascii_even)
'''

#49.wapt get the following  output
'''
inp='abcd'
ex_output={'a':97,'b':98,'c':99,'d':100}
out={}
i=0
while i<len(inp):
    out[inp[i]]=ord(inp[i])
    i+=1
print(out)
'''

#50.wapt get the following output
'''
inp='hello'
ex_out={0:'h',1:'e',2:'l',3:'l',4:'o'}
out={}
i=0
while i<len(inp):
    out[i]=inp[i]
    i+=1
print(out)
'''

#51.wapt get the following output
'''
inp=['hai',89,3.4,'hello',90,'py']
ex_output={'hai':'hi','hello':'ho','py':'py'}
out={}
i=0
while i in range(len(inp)):
    if type(inp[i])==str:
        out[inp[i]]=(inp[i][0]+inp[i][-1])
    i+=1
print(out)
'''

#52.wapt get the following output
'''
inp='hai hello'
ex_out='olleh iah'
i=0
out=''
while i<len(inp):
    out=inp[i]+out
    i+=1
print(out)
'''

#53.wapt count the no of vowels present in a given string
'''
inp='adafredsichinns322aIOWUBCauio'
i=0
c=0
while i<len(inp):
    if inp[i] in 'aeiouAEIOU':
        c+=1
    i+=1
print(c)
'''

#54.wapt get the following ouput
'''
inp='hai hello good morning'
ex={'hai':'a','hello':'l','good':'gd','morning':'n'}
inp=inp.split()
i=0
out={}
while i<len(inp):
    if (len(inp[i]))%2==0:
        out[inp[i]]=((inp[i][0])+(inp[i][-1]))
    else:
        out[inp[i]]=inp[i][(len(inp[i]))//2]
    i+=1
print(out)
'''

#55.wapt get the following output
'''
inp=['jiocinema.com','file.py','web.html']
ex_out=['com','py','html']
out=[]
i=0
while i<len(inp):
    j=0
    while j<len(inp[i]):
        if inp[i][j]=='.':
            out.append(inp[i][inp[i].index(inp[i][j])+1:])
        j+=1
    i+=1
print(out)           
'''

#56.wap to get the following output.
'''
inp=['jiocinema.com','file.py','web.html','amaxon.com','text.py']
ex_out={'com':['jiocinema','amazon'],'py':['file','text'],'html':['web']}
out={}
i=0
lst=[]
while i < len(inp):
    j=0
    while j<len(inp[i]):
        if inp[i][j]=='.':
            j=inp[i].index('.')
            out[inp[i][inp[i].index(inp[i][j])+1:]]=[]
        j+=1
    while k<len(inp(i)):
        if inp[i][j]=='.':
            j=inp[i].index('.')
            out[inp[i][inp[i].index(inp[i][j])+1:]]=out.append(inp[i][inp[i].index(inp[i][j])])   
        k+=1
    i+=1

print(out)
'''

#57.wapt get the following output
'''
inp=['jiocinema.com','file.py','web.html','amazon.com','text.py']
ex_out={'com':['jiocinema','amazon'],'py':['file','text'],'html':['web']}
out={}
l=len(inp)
i=0
while i<l:
    dot_pos=0
    curr_item=inp[i]
    j=0
    while j<len(curr_item):
        if curr_item[j]=='.':
            dot_pos=j
            ext=curr_item[dot_pos+1:]
            name=curr_item[:dot_pos]
            if ext not in out:
                out[ext]=[]
                out[ext].append(name)
            else:
                out[ext].append(name)
        j+=1
    i+=1
print(out)
'''

#58.wap to get the following output(count no of vowels)
'''
inp='hai hello how are you and'
ex_out={'hai': 2, 'hello': 2, 'how': 1, 'are': 2, 'you': 2, 'and': 1}
inp=inp.split()
i=0
out={}
while i<len(inp):
    j=0
    c=0
    while j < len(inp[i]):
        if inp[i][j] in 'aeiouAEIOU':
            c+=1   
        j+=1
        out[inp[i]]=c
    i+=1
print(out)
'''

#59.wapt extract all the string values present in the list collection only
#if the last char is uppercase.concatenate the extracted output using '*'
'''
inp=['hai','hellO','how','Are','yoU','DAY','Done']
ex_out='hellO*yoU*DAY'
out=''
l=len(inp)
i=0
while i<l:
    if inp[i][-1].isupper():
        if len(out)==0:
            out=inp[i]
        else:
            out+='*'+inp[i]
    i+=1
print(out)
'''

#60.wapt extract all the list data items  present in list collection
#only if it is having middle value,that value is integer and having even
#number at start
'''
inp=['hllo1llll','1hi','1hi2oij']
ex_out=['1hi2oij']
out=[]
i=0
while i<len(inp):
    if len(inp[i])%2==1 and (inp[i][(len(inp[i])//2)]).isdigit() and (inp[i][0]).isdigit():
        out.append(inp[i])
    i+=1
print(out)
'''


#61.wap to get the following output
'''
inp='just looking like a wow'
ex_out='jusT LOOKING Like a wow'
w=inp.split()
out=[]
i=0
while i<len(w):
    if i==0:
        w[i]=w[i][:-1]+w[i][-1].upper()
    elif i==1:
        w[i]=w[i].upper()
    elif i==2:
        w[i]=w[i].capitalize()
    else:
        w[i]=w[i]
    i+=1
print(' '.join(w))
'''

#62.waptf the common elements in two sets using while
'''
set1={1,2,3,4,5}
set2={3,4,5,6,7}
i=0
set3=set()
s1=list(set1)
s2=list(set2)
if len(s1)>len(s2):
    n=len(s1)
else:
    n=len(s2)
while i<n:
    if s1[i] in s2:
        set3.add(s1[i])
    i+=1
print(set3)
'''

#63.waptc if a no is a perfect no or not   try --> 6,28,496 perfect no's
'''
n=int(input('enter a number'))
i=1
s=0
while i<n:
    if n%i==0:
        s+=i
    i+=1
if n==s:
    print(n,'is a perfect no')
else:
    print(n,'is not a perfect no')
'''

#64.waptf the length of the longest substring without repeating characters in a
#given string using while loop
''' not done
s='abcabcabc abcd aabbcc'
st=s.split()
i=0
c=0
l=0
while i<len(st):
    j=0
    no_re=set(st[i])
    while j<len(st[i]):
        if st[i][j] not in list(no_re):
            c+=1
        if len(st[i]) - c > l:
            l=len(st[i])-c
        j+=1
        
    i+=1
    c=0
'''

#65.waptf the max and min elements in a tuple using while loop
'''
a=(1,2,4394,0,23,832)
i=0
l=len(a)
ma=a[0]
mi=a[0]
while i<l:
    if a[i]<mi:
        mi=a[i]
    elif a[i]>ma:
        ma=a[i]
    i+=1
print('min',mi)
print('max',ma)
'''

#66.waptf the union,intersection and difference of two sets using while loop
'''
s1={1,2,3,4}
s2={3,4,5,6}
s1=list(s1)
s2=list(s2)
if len(s1)>len(s2):
    l=s1
    s=s2
else:
    l=s2
    s=s1
i=0
while i<len(l):
    if s[i] in l:
        print(s[i],end=' ')
    i+=1
print()
i=0
while i<len(l):
    if s[i] not in l:
        print(s[i],end=' ')
    if l[i] not in s:
        print(l[i],end=' ')
    i+=1
    
print()
u=set(s1+s2)
print(u)
'''

#67.waptc the no of occurrences of each character in a string using a dictionary and while loop
'''
s='aaabbbabaccabbcd'
i=0
c={}
while i<len(s):
    if s[i] not in c:
        c[s[i]]=1
    elif s[i] in c:
        c[s[i]]+=1
    i+=1
print(c)
'''

#68.wapt remove duplicate value from collection without converting to set
'''
inp='abcdsdcsa'
out=''
i=0
while i<len(inp):
    if inp[i] not in out:
        out+=inp[i]
    i+=1
print(out)
'''

#69.waptf the length of collection without using len function
'''
inp='abcdsdcsa'
i=0
while 1:
    try:
        if inp[i] in inp:
            pass
    except:
        break
    i+=1
print(i)
'''

#72.wapt extract all the integers from a list only if the integer is starting
#from even number and ending as odd number and having length more than 3
'''
inp=[2321,1322,231,41,12234,12231,4031,2349483]
i=0
out=[]
print(inp)
while i<len(inp):
    j=0
    n=inp[i]
    c=0
    while n!=0:
        r=n%10
        c+=1
        n=n//10
        if c>3 and inp[i] not in out and (inp[i]%10)%2!=0:
            out.append(inp[i])            
    i+=1
print(out)  #greater than 3 digits
i=0
while i<len(out):
    j=0
    n=out[i]
    r=0
    while n!=0:
        r=n%10
        n=n//10
    if r%2!=0:
        out.remove(out[i])
    i+=1
print(out)    
'''


#71.wapt extract all the individual data items of a list if the length of
#extracted output is more than 4 print first value of the output else print
#last value of the output list and add 10 to it

#72.wapt get the following output
'''
inp1='11001010'
inp2='01110010'
ex_out=4 #(to count how many positions are having same value)
i=0
out=0
if len(inp1)==len(inp2):
    while i<len(inp1):
        if inp1[i]==inp2[i]:
            out+=1
        i+=1
print('out =',out)
'''

#73.wapto get the following output
'''
inp=[1,2,3,4,5,6]
val=3
#ex_out=[1,2,3][4,5,6]
vall=2
#ex_out=[1,2][3,4][5,6]
i=0
out=[]
while i<len(inp):
    if i>=val:
        if len(out)==val:
            print(out,end='')
            out=[]
    out+=[inp[i]]
    i+=1
print(out)
'''

#74.waptc weather the given number is spy number or not i.e, 1*2*3=1+2+3
#1,2,3,4,5,6,7,8,9,22,123,132,213,231,312,321 are spy numbers
'''
p=1
s=0
c=n=132
while n!=0:
    r=n%10
    p*=r
    s+=r
    n=n//10
if p==s:
    print(c,'is a spy number')
else:
    print(c,'is not a spy number')
'''

#75.write a program to check whether the given number is Xylem number or not
#i.e, 1234-->1+4=2+3   1111,121,132,231,143
'''
le=0
ri=0
c=n=121
i=1
while n!=0:
    if i==1:
        r=n%10
        n=n//10
        ri+=r
        i+=1
    r=n%10
    n=n//10
    if n==0:
        ri+=r
    else:
        le+=r
if ri==le:
    print(c,'Xylem number')
else:
    print(c,'not a Xylem number')
'''

#76.waptc weather the given no is a ploem number or not
#i.e 12345-->1+5!=2+3+4
'''
le=0
ri=0
i=1
c=n=12345
while n>0:
    if i==1:
        r=n%10
        n=n//10
        ri+=r
        i+=1
    r=n%10
    n=n//10
    if n==0:
        ri+=r
    else:
        le+=r
if ri!=le:
    print(c,'ploem number')
else:
    print(c,'not a ploem number')
'''

#77.waptc weather the given number is neon number or not
#i.e 9 is number,9**2=81-->8+1=9    0,1,9
'''
c=n=9
s=0
n=n**2
while n>0:
    r=n%10
    s+=r
    n=n//10
if c==s:
    print(c,'is a neon number')
else:
    print(c,'is not a neon number')
'''

#78.waptc weather the given number is automorphic or not
#i.e 5 is number 5**2=25 last digit of 25 is the number itself
'''
n=5 #6
sq=n**2
i=0
while i<1:
    r=sq%10
    if r==n:
        print(n,'is a automorphic no')
    else:
        print(n,'is not a automorphic no')
    i+=1
'''
#79.wapt count the no of words in the given string
'''
s=input('enter the str:').split()
i=0
c=0
while 1:
    try:
        if s[i] in s:
            i+=1
    except:
        break
print(i)
'''
    
#80.waptf the length of the longest word
'''
s=input('enter a sentence').split()
i=0
while i<len(s):
    j=0
    l=0
    while j<len(s[i]):
        j+=1
    if j-1>l:
        l=j-1
    i+=1
print(j)
'''

#81.wapt count number of consonants in the given string
#s=input('enter the str:')
'''
s=input('enter a string')
i=0
c=0
while i<len(s):
    if s[i] not in 'aeiouAEIOU':
        c+=1
    i+=1
print(c)
'''

#82.waptc the type of data entered by the users
#inp=eval(input('enter a input'))

#83.waptc weather the given tuple is palindrome or not
'''
inp=('a',1,3,2,4,2,3,1,'a')
#inp=('a',1,3,2,4,2,3,'a')
rev=inp[::-1]
i=0
res=True
while i<len(inp):
    if inp[i]==rev[i]:
        res*=True
    else:
        res*=False
    i+=1
if res==True:
    print(inp,'is a palindrom')
else:
    print(inp,'is not a palindrom')
'''

#84.waptc weather the given collection is having nested collection or not
'''
inp=eval(input('enter a collection'))
i=0
while i<len(inp):
    if type(inp[i]) in (list,tuple,set,dict):
        print('the collection contains nested collection')
        break
    i+=1
if i==len(inp):
    print('the collection does not contains nested collection')
'''
#85.wapt return the positions of vowels present in the given string
'''
inp=input('enter a string')
i=0
while i<len(inp):
    if inp[i] in 'aeiouAEIOU':
        print(i,end=' ')
    i+=1
'''
#86.waptf the length of collection without using len function
'''
inp=eval(input('enter a collection'))
i=0
while 1:
    try:
        if inp[i] in inp:
            i+=1
    except:
        break
print(i)
'''

#87.waptc weather the entered username and password is correct or not
#if not correct print enter again
'''
name=input('enter your name')
pass_w=int(input('enter password'))
data={'Bhoopal':1234,'amruth':2345}
while 1:
    if name in data.keys():
        if pass_w==data[name]:
            print('login successful')
            break
        else:
            name=input('enter your name')
            pass_w=int(input('enter password'))
    else:
        name=input('enter your name')
        pass_w=int(input('enter password'))
'''

#88.wapt extract all integer data items from tuple
'''
tup=(1,"hi",'hello',232,32.23)
i=0
while i<len(tup):
    if type(tup[i])==int:
        print(tup[i],end=' ')
    i+=1
'''
#89.wapt extract all the non default values from the list
'''
lst=[1,'hai',0,' ',0.0,(),'hello','']
i=0
while i<len(lst):
    if bool(lst[i])==True:
        print(lst[i],end=' ')
    i+=1
'''

#90.wapt get the following output
#inp='hai hello how are you'
#out='hai**hello**how**are**you'
'''
inp='hai hello how are you'
o=''
a=len(inp)
i=0
while i<a:
    if inp[i].isspace():
        o+='**'
    else:
        o+=inp[i]
    i+=1
print(o)

'''

#91.wapt reverse the given list
'''
lst=[1,'hai',0,' ',0.0,(),'hello','']
i=0
out=[]
while 1:
    out=lst[::-1]
    break
print(out)
'''
  
#92.wap for number game
'''
import random
n=int(input("enter a number between 1 t0 100:"))
count=0
count=0
while 1:
    guess=random.randint(0,100)
    if guess>n:
        print('the guess is too high')
        count+=1
        n=int(input("enter a number between 1 t0 100:"))

    elif guess<n:
        print('the quess is too low')
        count+=1
        n=int(input("enter a number between 1 t0 100:"))

    else:
        print('correct, but you took',count,'attempts')
        break
'''       
#93.waptp thank you for n times

'''
n=int(input('enter a no'))
i=1
while i<=n:
    print(i,'Thank you')
    i+=1
''' 
    
