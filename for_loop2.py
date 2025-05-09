'''
Ay Bx Cw Dv Eu 
Ft Gs Hr Iq Jp 
Ko Ln Mm Nl Ok 
Pj Qi Rh Sg Tf 
Ue Vd Wc Xb Ya

below program gives the output for the above pattern
'''
'''
for i in range(ord('A'),ord('Z')):
    if i%5!=0:
        print(chr(i)+chr(186-i),end=' ')
    else:
        print()
        print(chr(i)+chr(186-i),end=' ')
'''
#-------------------------------------------------------------

'''
A B C D E 
F G H I J 
K L M N O 
P Q R S T 
U V W X Y
below program gives the output for the above pattern
'''
'''
for i in range(ord('A'),ord('Z')):
    if i%5!=0:
        print(chr(i),end=' ')
    else:
        print()
        print(chr(i),end=' ')
'''

#6/2/2025
'''
1 11 111 1111 11111
sum
'''
'''
n=int(input('enter n value:'))
s=0
for i in range(1,n+1):
    print(i*'1', end=' ')
    s+=int('1'*i)
print()
print(f'sum is {s}')
'''

'''
give roman numbers of given number
1 2 3
I II III IV V ------
n=input('enter the integer value')
d={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',0:'0'}
for i in n:
    print(d[int(i)],end=' ')
'''
#reversing the dictionary
#d={'a':97,'b':98,'c':99,'d':100,'e':101}
#output={'e': 101, 'd': 100, 'c': 99, 'b': 98, 'a': 97}
'''
d={'a':97,'b':98,'c':99,'d':100,'e':101}
out={}
t=list(d)
for i in range(len(t)-1,-1,-1):
    out[t[i]]=d[t[i]]
print(out)
'''

#key value exchange in dictionary
#d={'a':97,'b':98,'c':99,'d':100,'e':101}
#output={97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e'}
'''
d={'a':97,'b':98,'c':99,'d':100,'e':101}
out={}
t=list(d)
for i in range(len(t)):
    out[d[t[i]]]=t[i]
print(out)
'''

#7/2/2025

#
'''
import random
print("hey.... I am guessing number between 1-100")
c=random.randint(1,100)
for i in range(5,0,-1):
    guess=int(input("what have you guessed:(give only integers)"))
    if c==guess:
        print("correct answer, you won the game")
        break
    else:
        print(f"sorry, it was a wrong guess\n you have {i-1} life left\n")
    if i==1:
        print(f'the number was:{c}')
        print("you lost the game....")
'''
#prime number checking
'''
inp=int(input("enter a number"))
c=0
for i in range(2,inp//2+1):
    if inp%i==0:
        print('not prime')
        break
else:
    print('prime')
'''

'''

n=10
if n<20:
    print(n)
else:
    break

the above 

Break
->break is a keyword which is used to terminate the execution of loops where ever it is necessary
->break statement can be used for both while loop and for loop

->break statement can be written directly inside the loop without any condition but it is of no use
    where it should be written with valid condition for its propper execution
for i in range(1,101):
    break
print(i)

->break statements can not be written without using looping statements
n=10
if n<20:
    print(n)
else:
    break

the above program will gives error

->

'''
#wap to find the smallest factor any odd number except 1
'''
n=int(input('enter the number'))
if n%2==1:
    for i in range(2,n):
        if n%i==0:
            print(i)
            break
'''

#the highest factor
'''
n=int(input("enter a number"))
for i in range(n-1,1,-1):
    if n%i==0:
        print(i)
        break
    '''
            
#the highest common factor
'''
n=int(input("enter 1st number"))
m=int(input("enter 2nd number"))
t=0
if n<m:
    t=n
else:
    t=m
hcf=1
for i in range(1,t+1):
#for i in range(t,0,-1):

    if n%i==0 and m%i==0:
        hcf=i
        #break
print(hcf)
'''


#wap find the least common multiple
'''n=int(input('enter 1st number:'))
m=int(input('enter 2nd number:'))
t=0
if n>m:
    t=n
else:
    t=m
lcm=1
for i in range(t,n*m):
    if i%n==0 and i%m==0:
        lcm=i
        break
print(lcm)
'''

#wap find the least common multiple
#lcm*hcf=n*m    lcm=(n*m)//hcf
'''
n=int(input('enter 1st number:'))
m=int(input('enter 2nd number:'))
t=0
if n<m:
    t=n
else:
    t=m
hcf=1
for i in range(t,0,-1):
    if n%i==0 and m%i==0:
        hcf=i
        break
print((n*m)//hcf)
'''

#8/2/2025

#continue      without loops we cannot use it
#continue
'''
continue is a keyword which is used to skip the current execution and to make the control
to go for the next iteration
->continue statements cannot be used without using looping statements
->examples are given below
'''
'''
for i in range(1,21):
    #if i==2:
    if i in (2,3,4,5,6):
        continue
    else:
        print(i)
    '''
'''
for i in range(1,101):
    continue
print(i)
'''

#even numbers
'''
for i in range(1,21):
    if i%2==1:
        continue
    else:
        print(i)
'''


#pass            we can use it anywhere even if there is no loops
#     used to overcome the errors
#pass
'''
pass is a keyword which is used to keep an empty block as a valid block without
throwing any error
->we can use pass inside decisional or conditional statements, looping statements,
functions and classes
'''

'''
for i in range(1,101):
    pass   #used to overcome the errors 
print(i)
'''
'''
n=10
if n<15:
    pass
else:
    print(i)
'''

'''
n=int(input('enter no of rows for start pattern:'))
for i in range(1,n+1):
    print(i*'*')
*
**
***
****
*****
'''
'''
n=int(input('enter no of rows for start pattern:'))
for i in range(n,0,-1):
    print(i*'*')

*****
****
***
**
*
'''
'''
n=int(input('enter no of rows for start pattern:'))
for i in range(1,n+1):
    print(' '*(n-i)+i*'*')
    
    *
   **
  ***
 ****
*****
'''
'''
n=int(input('enter no of rows for start pattern:'))
for i in range(n,0,-1):
    print(' '*(n-i)+i*'*')
*****
 ****
  ***
   **
    *
'''

'''
n=int(input('enter no of rows for start pattern:'))
t=n
for i in range(1,(n)*2,2):
    print(' '*(t)+i*'*')
    t-=1

     *
    ***
   *****
  *******
 *********
'''
'''
n=int(input('enter no of rows for start pattern:'))
t=1
for i in range(((n)*2)-1,0,-2):
    print(' '*(t)+(i*'*'))
    t+=1


 *********
  *******
   *****
    ***
     *
'''

'''
n=int(input('enter no of rows for start pattern:'))
t=n
for i in range(1,n*2,2):
    print(' '*(t)+i*'*')
    t-=1
t=1
for i in range((n*2)-3,0,-2):
    print(' '*(t)+' '+(i*'*'))
    t+=1

     *
    ***
   *****
  *******
 *********
  *******
   *****
    ***
     *
'''
'''
n=int(input('enter no of rows for start pattern:'))
for i in range(1,n+1):
    print(' '*(n-i)+i*('* '))

    * 
   * * 
  * * * 
 * * * * 
* * * * *
'''
'''
n=int(input('enter no of rows for start pattern:'))
for i in range(n,0,-1):
    print(' '*(n-i)+'* '*i)

* * * * *
 * * * *
  * * *
   * *
    *
'''
'''
for i in range(1,5):
    print(' '*(5-i)+'* '*i)
for i in range(5,0,-1):
    print(' '*(5-i)+'* '*i)
    
    
    *
   * * 
  * * *  
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
'''
'''
j=7
for i in range(1,8):
    print(('* '*i)+(j-1)*'  '+('* '*i))
    #print(('* '*i)+(j-1)*'  '*2+('* '*i))
    j-=1
'''

'''
*             * 
* *           * * 
* * *         * * * 
* * * *       * * * * 
* * * * *     * * * * * 
* * * * * *   * * * * * * 
* * * * * * * * * * * * * * 
'''
'''
j=7
for i in range(1,8):
    print(('* '*i)+(j-1)*'  '*2+('* '*i))
    j-=1
    
*                         * 
* *                     * * 
* * *                 * * * 
* * * *             * * * * 
* * * * *         * * * * * 
* * * * * *     * * * * * * 
* * * * * * * * * * * * * * 
'''
'''
ch=64
for i in range(1,5+1):
    print((chr(ch+i)+' ')*i)
A 
B B 
C C C 
D D D D 
E E E E E
'''
'''
n=int(input('enter no of rows: '))
for i in range(1,n+1):
    for j in range(i):
        print(chr(65+j),end=' ')
    print()

A 
A B 
A B C 
A B C D 
A B C D E 
'''

'''
n=int(input('enter no of rows: '))
ch=65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end=' ')
        ch+=1
    print()

A 
B C 
D E F 
G H I J 
K L M N O
'''
'''
n=int(input('enter no of rows: '))
ch=48
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch),end=' ')
        ch+=1
    print()

0 
1 2 
3 4 5 
6 7 8 9

'''

#perfect number for the given range
'''
for i in range(1,10):
    sum=0
    for j in range(1,i):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i,end=' ')
'''
#armstrong number
'''
summ=0
for i in range(1,1000):
    n=i
    while(i):
        r=i%10
        summ+=r**len(str(n))
        i=i//10
    if summ==n:
        print(n)
    summ=0
'''
'''
for i in range(1,1001):
    p=len(str(i))
    sum=0
    for j in str(i):
        sum+=int(j)**p
    if sum==i:
        print(i)
'''

'''
inp=['python','is','good']
ex_out=['pythn','s','gd']
op=[]
for i in range(len(inp)):
    o=''
    for j in inp[i]:
        if j not in 'aAeEiIoOuU':
            o+=j
    op.append(o)
print(op)
'''
'''
ip=5553433444445555
ex_out=5
inp=str(ip)
d={}
c=1

for i in inp:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    c=max(c,d[i])
key=list(d.keys())
value=list(d.values())
i=value.index(c)
print(key[i])
'''
'''
inp='5553433444445555'
ex_out=5
out=''
t=0
for i in inp:
    c=0
    for j in inp:
        if i==j:
            c+=1
    if c>t:
        t=c
        out=i
print(out)
'''
#
'''
inp='aaaaabbbbcccdaadd'
expected_out='a7b4c3d3'
out=''
for i in inp:
    c=0
    for j in inp:
        if i==j:
            c+=1
    if c>1 and i not in out:
        out+=i+str(c)
print(out)
'''

#11/2/2025    pattern programming
'''
for i in range(1,11):
    print(i,end=' ')
'''


'''
*****
*****

matrix 2x5
'''
'''
for i in range(2):
    for j in range(5):
        print('*',end='')
    print()
    '''
'''
for i in range(2):
    for j in range(5):
        print(j+2,end=' ')
    print()
'''
'''
n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * 
*       * 
*       * 
*       * 
* * * * * 

'''
'''
n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
'''
'''
    
  * * *   
  * * *   
  * * * 

'''
'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print(j,end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
1 2 3 4 5
1       5
1       5
1       5
1 2 3 4 5
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print(i,end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
1 1 1 1 1
2       2
3       3
4       4
5 5 5 5 5
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print(i+j,end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
2 3 4 5 6
3       7
4       8
5       9
6 7 8 9 10
'''
'''
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or j==0 or j==4:
            print(i*j,end=' ')
        else:
            print(' ',end=' ')
    print()
    '''
            
'''
0 0 0 0 0
0       4
0       8
0       12
0 4 8 12 16
'''

'''
for i in range(5):
    for j in range(5):
        if i==0 or i==2 or i==4 or j==0 or j==2 or j==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#(n+1)//2==i or (n+1)//2==j
'''
* * * * * 
*   *   * 
* * * * * 
*   *   * 
* * * * * 
'''

'''
for i in range(5):
    for j in range(5):
        if i==0 or i==4 or i==j or j==0 or j==4 or (i+j)==4:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#i==j or (i+j)==4
'''
* * * * * 
* *   * * 
*   *   * 
* *   * * 
* * * * *
'''
'''
for i in range(1,6):
    for j in range(1,6):   
        print(str(i)+str(j),end=' ')
    print()
11 12 13 14 15 
21 22 23 24 25 
31 32 33 34 35 
41 42 43 44 45 
51 52 53 54 55 
'''

'''
su=0
for i in range(1,200):
    n=i
    while(i):
        r=i%10
        s=r**len(str(n))
        su=su+s
        i=i//10
    if su==n:
        print(su)
    su=0
'''

'''
su=0
for i in range(1,1001):
    n=i
    for j in str(i):
        s=int(j)**len(str(n))
        su+=s
    if su==n:
        print(su)
    su=0
'''
'''
su=0
for i in range(1,1000):
    ch=i
    for j in range(1,i):
        if i%j==0:
            su+=j
    if su==ch:
        print(su)
    su=0
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        elif i==j or (i+j)==n+1:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()
'''
'''
* * * * * 
*   *   * 
* *   * * 
*   *   * 
* * * * *
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(' ',end=' ')
        elif i==j or (i+j)==n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
5
          
  *   *   
    *     
  *   *
  
'''
'''
n=int(input('enter'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i ==1 or j==1:
            print(i+j,end=' ')
        elif i==n or j==n:
            print(i+j,end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#12/2/2023 wednesday
#LOGIC hiding OR skipping the same index and mul with remaining int values
'''
inp=[2,3,1,True,'hello',3]
ex_out=[9,6,18,18,18,6]
out=[]
for i in range(len(inp)):
    p=1
    for j in range(len(inp)):
        if i!=j and type(inp[j])==int:
               p*=inp[j]
    out.append(p)
print(out)
'''

'''
inp=[RCB,CSK,SRH,MI,KKR,GT,RR]
RCB vs CSK
RCB vs SRH
BUT NOT CSK vs RCB IF ALREADY RCB VS CSK IS SHEDULED
output should be in both sql and python
'''
'''
inp=['RCB','CSK','SRH','MI','KKR','GT','RR']
for i in range(len(inp)):
    for j in range(len(inp)):
        if i<j:
            print(f'{inp[i]} vs {inp[j]}')
'''

'''
in sql
CREATE TABLE IPL(TID NUMBER(10),NAME VARCHAR(20));
INSERT INTO IPL VALUES(1,'RCB');
INSERT INTO IPL VALUES(2,'CSK');
INSERT INTO IPL VALUES(3,'MI');
INSERT INTO IPL VALUES(4,'SRH');
INSERT INTO IPL VALUES(5,'KKR');
INSERT INTO IPL VALUES(6,'GT');
INSERT INTO IPL VALUES(7,'RR');
 SELECT * FROM IPL P1,IPL P2;
 SELECT * FROM IPL P1,IPL P2 WHERE P1.TID < P2.TID;
SELECT P1.NAME||' VS '||P2.NAME FROM IPL P1,IPL P2 WHERE P1.TID < P2.TID;
'''
'''
n=int(input())
c=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(c,end='  ')
        c+=1
    print(\n\n)
'''
'''
1  2  3  4  5 
6  7  8  9  10 
11 12 13 14 15 
16 17 18 19 20 
21 22 23 24 25 
'''
'''
for i in range(1,6):
    for j in range(1,6):
        print(i,end=' ')
    print()
'''
'''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5
'''
'''
for i in range(1,6):
    for j in range(1,6):
        print(j,end=' ')
    print()
'''
'''
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5
'''
'''
#identical matrix
for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
'''
'''
1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if (i+j)==6:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
    '''
'''
0 0 0 0 1 
0 0 0 1 0 
0 0 1 0 0 
0 1 0 0 0 
1 0 0 0 0 
'''
'''
for i  in range(1,6):
    for j in range(1,6):
        if i==j or (i+j)==6:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
'''
'''
1 0 0 0 1 
0 1 0 1 0 
0 0 1 0 0 
0 1 0 1 0 
1 0 0 0 1 
'''

#13/2/2025 Thursday


'''
for i in range(1,6):
    for j in range(1,6):
        #print(f'{i}{j}',end=' ')
        print(i,j,sep='',end=' ')
    print()
'''
'''
11 12 13 14 15 
21 22 23 24 25 
31 32 33 34 35 
41 42 43 44 45 
51 52 53 54 55
'''
'''
for i in range(1,6):
    for j in range(1,6):
        #print(f'{i}{j}',end=' ')
        if i==1:
            print('* ',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''

*  *  *  *  *  
21 22 23 24 25 
31 32 33 34 35 
41 42 43 44 45 
51 52 53 54 55
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if j==1 or j==5:
            print('* ',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
*        *  
*        *  
*        *  
*        *  
*        * 
'''
'''
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
* * * * * * * * * 
                  
                  
                  
                  
                  
                  
                  
* * * * * * * * *
'''
'''
#A
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or j==1 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

'''
'''
#B
n=10
for i in range(1,n):
    for j in range(1,n):
        if j==1 or i==n-1 or i==1 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
#C
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1 or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
#D
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1 or j==n-1 or j==2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#E
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1 or j==1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#F
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or j==1 or (i==n//2 and j<=n//2+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#G
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-3 or (j==1 and i<=n-3) or (i==n//2 and j>=n//2) or (j==n-1 and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#H
n=10
for i in range(1,n):
    for j in range(1,n):
        if j==1 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#I
n=10
for i in range(1,n):
    for j in range(1,n):
        if  i==n-1 or i==1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#J
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or j==n//2 or (i==n-1 and j<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#k
n=10
for i in range(1,n):
    for j in range(1,n):
        if j==n//2 or ((i+j)==n and j>=n//2) or (i==j and j>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#L
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==n-1 or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#M
n=10
for i in range(1,n):
    for j in range(1,n):
        if  j==1 or j==n-1 or (i==j and j<=n//2) or ((i+j)==n and j>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
#N
n=10
for i in range(1,n):
    for j in range(1,n):
        if j==1 or j==n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#O
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1 or j==1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#P
n=10
for i in range(1,n):
    for j in range(1,n):
        if (i==1 and j>=n//2) or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#Q
n=10
for i in range(1,n):
    for j in range(1,n):
        if (i==1 and 2<=j<=n-2) or (i==n-2 and 2<=j<=n-2) or (j==n-2 and 1<=i<=n-2) or (j==2 and 1<=i<=n-2) or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#R
n=10
for i in range(1,n):
    for j in range(1,n):
        if  j==n//2 or (i==1 and j>=n//2) or (j==n-1 and i<=n//2) or (i==n//2 and j>=n//2) or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#S
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1 or (j==1 and i<=n//2) or i==n//2 or (j==n-1 and i>=n//2) or (j==n-1 and i<=2) or (j==1 and i>=n-2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#T
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#U
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==n-1 or j==1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''

#V
n=5
for i in range(1,n+1):
    for j in range(1,n*2+1):
        if i%2==0: #skipping the lines
            pass
        elif (i==j and j<=(n*2)//2) or (i+j==n*2 and i<=(n*2)//2):
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
'''
#V
n=5
s=n
l=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if (j==1 and i<=n//2+1) or (j==n and i<=n//2+1) or (i>=n//2+1 and j==s) or (i>=n//2 and j==l):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    if i>=n//2+1:
        l+=1
        s-=1
    print()
'''
'''
#W
n=10
for i in range(1,n):
    for j in range(1,n):
        if j==1 or j==n-1 or (i+j==n and j<=n//2) or (i==j and j>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#X
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==j or i+j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#Y
n=10
for i in range(1,n):
    for j in range(1,n):
        if (i==j and j<=n//2) or (i+j==n and j>=n//2) or (j==n//2 and i>=n//2): 
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#Z
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n-1 or i+j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''


#14/2/2025

#APPU
'''
n=10
for i in range(1,n):
    for j in range(1,n):
        if i==1 or j==1 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n//2 or j==1 or (j==n-1 and i<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==n//2 or j==1 or (j==n-1 and i<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
for i in range(1,n):
    for j in range(1,n):
        if i==n-1 or j==1 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#B
#H
#O
#O
#P
#A
#L
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==(n+1)//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==(n+1)//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==(n+1)//2 or j==1 or (j==n-1 and i<=(n+1)//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or j==n or i==(n+1)//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
print()

'''

'''
#BHOOPAL
n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==(n+1)//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(end=' ')
            
    for j in range(1,n+1):
        if j==1 or j==n or i==(n+1)//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(end=' ')
    
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(end=' ')

    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(end=' ')

    for j in range(1,n+1):
        if i==1 or i==(n+1)//2 or j==1 or (j==n-1 and i<=(n+1)//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(end=' ')
            
    for j in range(1,n+1):
        if i==1 or j==1 or j==n or i==(n+1)//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(end=' ')

    for j in range(1,n+1):
        if i==n or j==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print(end=' ')

    print()
'''

#15/2/2025
'''
#7
n=10
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or (i+j==n+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
#|\/|
#|/\|
n=11
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or i==j or (i+j==n+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=11
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==n or ((i+j)>=n+1 or i>=j) and (i+j<=n+1 or j>=i):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i+j==n+1 or i==j or (i<=j and i<=(n+1)//2 and i+j<=n+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
n=11
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or\
           (i>=j and i<=(n+1)//2) or (j>=(n+1)//2 and (i+j)<=n+1)\
           or (j<=(n+1)//2 and i+j>=n+1) or (i>=(n+1)//2 and i<=j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#17/2/2025
'''
n=input('enter a name:')
for i in range(len(n)):
    for j in range(len(n)):
        if j<=i:
            print(n[j],end=' ') 
    print()
'''
'''
B 
B h 
B h o 
B h o o 
B h o o p 
B h o o p a 
B h o o p a l
'''
'''
n=input('enter a name:')
c=len(n)-1
for i in range(len(n)):
    print(' '*c*2,end=' ')
    for j in range(i+1):
        print(n[j],end=' ')
    print()
    c-=1
'''
'''
             b 
           b h 
         b h o 
       b h o o 
     b h o o p 
   b h o o p a 
 b h o o p a l 
'''
'''
n=input('enter a name:')
c=len(n)-1
for i in range(len(n)):
    print(' '*c,end=' ')
    for j in range(i+1):
        print(n[j],end=' ')
    print()
    c-=1
''' 
'''
       b 
      b h 
     b h o 
    b h o o 
   b h o o p 
  b h o o p a 
 b h o o p a l
'''
'''
n=11
for i in range(n):
    for j in range(n):
        if i+j>=n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=11
for i in range(n):
    for j in range(n):
        if i+j<=n-1 or i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=11
for i in range(n):
    for j in range(n):
        if i+j==n-1 or (i>=j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=11
for i in range(n):
    for j in range(n):
        if i+j==n-1 or (i<=j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
n=11
for i in range(n):
    for j in range(n):
        if i+j==n-1 or (i<=j):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
n=11
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==(n+1)//2 or (i+j>(n+1)//2 and (j-i)<=n//2 and i<=(n+1)//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

'''
          *           
        * * *         
      * * * * *       
    * * * * * * *     
  * * * * * * * * *   
* * * * * * * * * * * 
          *           
          *           
          *           
          *           
          *  
'''

'''
n=7
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==(n+1)//2 or ((i-j)<=n//2 and i>=(n+1)//2 and (i+j)<=n*2-(n//2)):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
'''
      *       
      *       
      *       
* * * * * * * 
  * * * * *   
    * * *     
      *
'''

#18/2/2025
#pascals triangle
'''
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1
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

for i in out:
    for j in i:
        print(j,end=' ')
    print()

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
            t.append(out[i-1][j-1]+out[i-1][j])
    out.append(t)
#print(out)
c=len(out)
for i in out:
    print(' '*(c-1),end=' ')
    for j in i:
        print(j,end=' ')
    c-=1
    print()
'''



