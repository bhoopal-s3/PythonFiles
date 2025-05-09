#1.wap square of no
'''n=int(input("enter a number:"))
print(f'square of {n} is {n*n}')
'''

#2.wap find product of 2 nos
'''
m=float(input('enter 1st number:'))
n=float(input('enter 2nd number:'))
print(f'product of {m} and {n} is {m*n}')
'''

#3.wap reverse of string

# n=input('enter a string')
# print(n[::-1])


#4.wap to swap two variables

# a=input('enter a no')
# b=input('enter a no')
# a,b=b,a
# print(a,b)


#5.square root of a no
'''
import math
inp=int(input())
print(math.sqrt(inp))
'''

#6.area of triangle
'''
import math
s1=int(input())
s2=int(input())
s3=int(input())
s=(s1+s2+s3)/2
a=(s*(s-s1)*(s-s2)*(s-s3))
print(math.sqrt(a))
'''
#or
'''
b=float(input())
h=float(input())
print(0.5*b*h)
'''

#7.simple interest
'''
p=float(input())
t=float(input())
r=float(input())
si=(p*t*r)/100
print(si)
'''

#8.area of circle
'''
n=float(input())
print(3.14*n**2)
'''

#simple if

#11.wap to register for a company only if job loc is bangalore
'''
loc=input()
if loc.upper()=='bangalore'.upper():
	print('register for company')
'''

#12.waptc no is even
'''
n=int(input())
if n%2==0:
	print('even')
'''

#13.waptc no is odd
'''	
n=int(input())
if n%2!=0:
	print('odd'
'''

#14.waptc no is between 5 to 10
'''
n=float(input())
if n>=5 and n<=10:
	print('true')
'''

#15.waptc str is having more than 3 chars
'''
n=input()
if len(n)>3:
	print('true')
'''

#16.waptc if no is 4 digit
'''
n=int(input())
if len(str(n))==4:
	print('yes')
'''

#17.waptc char is vowel
'''
n=input()
if n in 'aeiouAEIOU':
	print('vowel')
'''

#18.waptc no is even & multiple of 5
'''
n=int(input())
if n%2==0 and n%5==0:
	print('true')
'''

#19.waptc given string is a str
'''
inp=eval(input())
if type(inp)==str:
	print('yes')
'''

#20.waptc if given string is a char
'''
inp=input()	
if len(inp)==1:
	print('it is a char')
'''

#21.waptc if given char is uppercase alph

# inp=input()
# if inp.isupper():
# 	print('s')


#22.waptc if given char is lowercase alph
'''
inp=input()
if inp.islower():
	print('s')
'''
#23.waptc if given char is digit

# inp=input()
# inpu=int(inp)
# if inpu.is_integer():
#     print('s')


#24.waptc if given char is alph
'''
inp=input()
if inp.isalpha():
	print('s')
'''

#24.waptc if given char is a spl char
'''
inp=input()
if inp.isalnum()==False:
	print('s')
'''

#25.waptc if inp is a collection of list
'''
inp=eval(input())
if type(inp)==list:
	print('s')
'''

#26.waptc if val is default
'''
inp=eval(input())
if bool(inp)==False:
	print('de')
'''

#27.waptc the list consist of even no of values
'''
inp=list(input())
if len(inp)%2==0:
	print('s')
'''

#28.waptc if list has middle value
'''
inp=eval(input())
if len(inp)%2==1:
    print('s')
'''

#29.waptc if inp is immutable
'''
inp=eval(input())
if type(inp) not in (list,set,dict):
	print('s')
'''

#30.waptc if inp is mutable
'''
inp=eval(input())
if type(inp) in (list,set,dict):
	print('s')
'''

#31.waptc if the inp is sigle value:
'''
inp=eval(input())
if type(inp) in (int,float,complex,bool):
	print('s')
'''

#32.waptc if the inp is mvdt
'''
inp=eval(input())
if type(inp) not in (int,float,complex,bool):
	print('s')
'''

#33.waptc if the inp no is only single digit
'''
inp=int(input())
if inp>-1 and inp<10:
	print('s')
'''

#if else

#34.waptc if the no is even or odd
'''
n=int(input())
if n%2==0:
    print('even')
else:
    print('odd')
'''

#35.waptc if data is mutable or immutable
'''
inp=eval(input())
if type(inp) in (list,set,dict):
    print('mutable')
else:
    print('immutable')
'''

#36.waptc if given data is svdt or mvdt
'''
inp=eval(input())
if type(inp) in (int,float,bool,complex):
    print('svdt')
else:
    print('mvdt')
'''

#37.waptc given char is a spt symbol or not
'''
inp=input()
if inp.isalnum()==False:
    print('spl')
else:
    print('no')
'''

#38.waptc given str is gaving middle chr or not
'''
inp=input()
if inp%2==1:
    print('yes')
else:
    print('no')
'''

#39.waptc 2 variables are pointing to same memory loc or not
'''
a=input()
b=input()
if id(a)==id(b):
    print('same')
else:
    print('no')
'''

#40.waptc if the 1st value present inside a given list is complex or not
#input=[3+4j, 3, 43]
#ex_out=complex
'''
n=eval(input())
if type(n[0])==complex:
    print('complex')
else:
    print('not')
'''

#41. write a program to take and consider a tuple collection consisting of only
#two values. check whether the taken tuple is homogeneous or not
'''
n=eval(input())
if len(n)==2:
    if type(n[0])==type(n[1]):
        print('homogeneous')
    else:
        print('heterogeneous')
'''
#42.waptc the given num is mul of 10 or not
'''
n=int(input())
if n%10==0:
    print('yes')
else:
    print('no')
'''

#43.wap to consider an integer no. if the no is even then print the square
#of the no else print the cube of the no.
'''
n=int(input())
if n%2==0:
    print(n**2)
else:
    print(n**3)
'''

#44.waptc whether the given string is palindrome or not
'''
n=input()
if n==n[::-1]:
    print('palindrome')
else:
    print('not a palindrome')
'''

#45.wapt condider string input, if it is having more than 3 characters then
#print length of the string else print string as it is
'''
n=input()
if len(n)>3:
    print(len(n))
else:
    print(n)
'''

#46.waptc the user is eligible to vote or not
'''
n=float(input())
if n>=18:
    print('eligible')
else:
    print('not eligible')
'''

#47.waptc the no is div by 7 or not
'''
n=int(input())
if n%7==0:
    print('yes')
else:
    print('no')
'''

#48.waptc the last digit of a number entered by the user is div by 3 or not
'''
n=input()
if int(n[-1])%3==0:
    print('s')
else:
    print('no')
'''

#49.wapc the year is leap year
'''
n=int(input())
if n%4==0:
    print('leap year')
else:
    print('not')
'''

#50. waptc whether a no is a 3 digit no or not
'''
n=int(input())
if n>99 and n<1000:
    print('s')
else:
    print('no')
'''

#51.waptof the largest no of 2 nos
'''
n=float(input())
m=float(input())
if n>m:
    print(f'{n} is large')
else:
    print(f'{m} is large')
'''

#52.waptc if no is +ve or -ve
'''
n=float(input())
if n>=0:
    print('positive')
else:
    print('negative')
'''

#53.waptc if no is biv by 2 & 3 both
'''
n=int(input())
if n%2==0 and n%3==0:
    print('both')
elif n%2==0:
    print('div by 2')
else:
    print('div by 3')
'''

#elif statement
#54.waptc the relation b/w 2 int nos
'''
a=int(input())
b=int(input())
if a==b:
    print('equal')
elif a>b:
    print(f'{a} is bigger')
else:
    print(f'{b} is bigger')
'''

#55.waptc if given char is uppercase or lowercase or number. if char is
#uppercase print uppercase, if char is lowercase print lowercase. if the
#char is a no, print the ascii no of it.
'''
ch=eval(input())
if type(ch)==str and ch.isupper():
    print('uppercase')
elif type(ch)==str and ch.islower():
    print('lowercase')
elif type(ch)==int:
    print(ord(str(ch)))
else:
    pass
'''

#56.waptc given chr is a vowel or consonent. if vowel store inside the list
#if consonent, display the ascii value of that char
'''
a=input()
o=[]
if a in 'aAeEiIoOuU':
    o.append(a)
    print(o)
elif a not in 'aAeEiIoOuU':
    print(ord(a))
else:
    pass
'''

#57.waptc if given char is upper.if s conv to low else prin LOWERCASE.
'''
a=input()
if len(a)==1 and a.isupper():
    print(a.lower())
elif len(a)==1 and a.islower():
    print('LOWERCASE')
'''

#58.waptc if given char is a no if s, print tha ascii value of that number.
'''
a=input()
if len(a)==1 and a.isnumeric():
    print(ord(a))
'''

#59.waptc if char is uppercase, print its lowercase char or if char is lowercase
#print its uppercase char or it given char is spl char print the char after
#adding 8 to the ascii value of that particual spl char
'''
a=input()
if len(a)==1 and a.isalpha() and a.isupper():
    print(a.lower())
elif len(a)==1 and a.isalpha() and a.islower():
    print(a.upper())
else:
    print('ascii of',a,'is',ord(a),'after adding 8 it is',8+ord(a))
'''

#60.waptc if last char of a given str is a spl chr or not
'''
a=input()
if a[-1].isalnum()==False:
    print('spl')
else:
    print('no')
'''

#61.waptc if the middle value of heterogeneous tuple collection is int or not
'''
a=eval(input())
if type(a)==tuple:
    if (len(a)%2==1):
        if type(a[len(a)//2])==int:
            print('data type is int and value is ',a[len(a)//2])
        else:
            print('not')
'''

#62.write a program to check if the given date is individual data type or not
'''
n=input()
if type(n) not in (str,tuple,list,set,dict):
    print('not')
else:
    print('individual dt')
'''

#66.waptc if given char is upper or lower or num or spl char
'''
a=input()
if len(a)==1 and a.isalpha() and a.isupper():
    print('upper')
elif len(a)==1 and a.isalpha() and a.islower():
    print('lower')
elif len(a)==1 and a.isnumeric():
    print('numeric')
elif len(a)==1 and (a.isalnum()==False):
    print('spl char')
'''

#67.waptf the greatest among 2
'''
a=float(input())
b=float(input())
if a>b:
    print(f'{a} is bigger')
else:
    print(f'{b} is bigger')
'''

#68.waptf the smallest among 3
'''
a=float(input())
b=float(input())
c=float(input())
if a<b and a<c:
    print(f'{a} is smaller')
elif b<a and b<c:
    print(f'{a} is smaller')
else:
    print(f'{c} is smaller')
'''

#69.waptf the greatest among 4
'''
a=float(input())
b=float(input())
c=float(input())
d=float(input())
if a>b and a>c and a>d:
    print(f'{a} is bigger')
elif b>a and b>c and b>d:
    print(f'{b} is bigger')
elif c>a and c>b and c>d:
    print(f'{c} is bigger')
else:
    print(f'{d} is bigger')
'''

#70.waptf the smallest among 4
'''
a=float(input())
b=float(input())
c=float(input())
d=float(input())
if a<b and a<c and a<d:
    print(f'{a} is smaller')
elif b<a and b<c and b<d:
    print(f'{b} is smaller')
elif c<a and c<b and c<d:
    print(f' {c} is smaller')
else:
    print(f'{d} is smaller')
'''

#71.wapt calculate the e-bill. According to , for 1st 100 units there is no
#charge, for next 100 units there is 5rs per unit and after 200units,
#the price is 10rs per unit. if the input is 350 then total bill amount is 200rs
'''
e=float(input('enter units cosumed:'))
if e<=100:
    print('no charge')
elif e>100 and e<=200:
    c=e-100
    print('charge is',c*5,'Rs')
elif e>200:
    c=e-200
    ch=100*5
    ch+=c*10
    print('charge is',ch,'Rs')
'''

#72.wapt accept per from user & display the grade according ,if marks is greater
#than 90, grade is A. if marks is greater than 80 and less then equals to 90,
#grade is B, if marks >= 60 & marks <=80 grade is C if < 60 grade is D
'''
n=float(input())
if n>90 and n<=100:
    print('Grade A')
elif n>80 and n<=90:
    print('Grade B')
elif n>=60 and n<=80:
    print('Grade C')
elif n<60 and n>=0:
    print('Grade D')
'''

#73.wapt accept the cost price of a bike & Display the road tax to be paid
#according to the following criteria if cost price is greater than one lac.
#the tax is 50%, if it is greater than 50000 & <= 100000 the tax is 10% &
#if it is <=50000 the tax is 5%
'''
n=float(input())
if n>100000:
    print('road tax =',n*0.5)
elif n>50000 and n<=100000:
    print('road tax =',n*0.1)
elif n<=50000:
    print('road tax =',n*0.05)
'''

#74.wapt accept a no from 1 to 7 and display the name of the day. like 1 for
#sunday, 2 for monday and so on.
'''
n=int(input())
if n==1:
    print('SUNDAY')
elif n==2:
    print('MONDAY')
elif n==3:
    print('TUESDAY')
elif n==4:
    print('WEDNESDAY')
elif n==5:
    print('THURSDAY')
elif n==6:
    print('FRIDAY')
elif n==7:
    print('SATURDAY')
'''

#75.WAPT accept a no from 1:00 to 12:00 and display name and month and days in
#that month like one for january and number of days 31 and so on
'''
n=int(input())
if n==1:
    print('1 for JANUARY and no of days 31')
elif n==2:
    print('2 for FEBRAUARY and no of days 28')
elif n==3:
    print('3 for MARCH and no of days 31')
elif n==4:
    print('4 for APRIL and no of days 30')
elif n==5:
    print('5 for MAY and no of days 31')
elif n==6:
    print('6 for JUNE and no of days 30')
elif n==7:
    print('7 for JULY and no of days 31')
elif n==8:
    print('8 for AUGAST and no of days 31')
elif n==9:
    print('9 for SEPTEMBER and no of days 30')
elif n==10:
    print('10 for OCTOBER and no of days 31')
elif n==11:
    print('11 for NOVEMBER and no of days 30')
elif n==12:
    print('12 for DECEMBER and no of days 31')
'''

#76.accept any city from the user & display monuments of that city. for
#Delhi is red fort,Agra- Taj mahal, jaipur- jal mahal
'''
n=input()
if n.upper()=='chennai'.upper():
    print('Chennai- marina beach')
elif n.upper()=='bangalore'.upper():
    print('Bangalore- Lal bhag')
elif n.upper()=='mumbai'.upper():
    print('Mumbai- India gate')
elif n.upper()=='delhi'.upper():
    print('Delhi- Red fort')
'''

#77.accept 3 sides of a triangle & check whether it is an equilateral,
#isosceles or scalene triangle
'''
a=float(input())
b=float(input())
c=float(input())
if a==b and a==c:
    print('equilateral triangle')
elif a==b or a==c or b==c:
    print('isosceler triangle')
else:
    print('scalene triangle')
'''

#nested if
#1.waptf the second greatest among 4 nos
'''
a=float(input())
b=float(input())
c=float(input())
d=float(input())
if a>b and a>c and a>d:
    if b>c and b>d:
        print(f'{b} is second large')
    elif c>b and c>d:
        print(f'{c} is second large')
    else:
        print(f'{d} is second large')
elif b>a and b>c and b>d:
    if a>c and a>d:
        print(f'{a} is second large')
    elif c>a and c>d:
        print(f'{c} is second large')
    else:
        print(f'{d} is second large')
elif c>a and c>b and c>d:
    if a>b and a>d:
        print(f'{a} is second large')
    elif b>a and b>d:
        print(f'{b} is second large')
    else:
        print(f'{d} is second large')
else:
    if a>b and a>c:
        print(f'{a} is second large')
    elif b>a and b>c:
        print(f'{b} is second large')
    else:
        print(f'{c} is second large')
'''

#2.waptc type of a given char
'''
a=input()
if len(a)==1:
    if 'A' <= a <='Z' or 'a' <= a <= 'z':
        print('alpha')
    elif '0' <= a <= '9':
        print('digit')
    elif a==' ':
        print('space')
    else:
        print('spl char')
'''

#3.wapt consider an int no. print happy if the no is div by 2. print SAD if the
#no is div by 5 and print square of the no only if it is div by seven else print
#the no as it is
'''
n=int(input())
if type(n)==int:
    if n%2==0:
        print('happy')
    elif n%5==0:
        print('SAD')
    elif n%7==0:
        print(n**2)
    else:
        print(n)
'''

#4.waptf small no among 3 nos
'''
a=float(input())
b=float(input())
ci=float(input())
if a<b and a<ci:
    print(a)
elif b<a and b<ci:
    print(b)
else:
    print(ci)
'''

#5.wapt consider inp as string. print as it is if it is plindrome.
#print rev string if it has even no of chars. print all the chars present
#at an odd index if the str is having an odd no of chars.
'''
a=input()
if a==a[::-1]:
    print(a)
elif len(a)%2==0:
    print(a[::-1])
else:
    print(a[1::2])
'''

#6.wapt print middle char. if given string only if it is upper case char
'''
a=input()
if len(a)%2==1:
    if a[len(a)//2].isupper():
        print(a[len(a)//2])
'''

#7.waptc if given char is vowel or consonant
'''
a=input()
if len(a)==1:
    if type(a)==str:
        if a in 'aAeEiIoOuU':
            print('vowel')
        else:
            print('consonant')
'''

#8.waptp the len of given data only if it is even
'''
a=input()
if len(a)%2==0:
    print(len(a))
'''

#9.waptc greatest among 3 nos using nested if
'''
a=float(input())
b=float(input())
c=float(input())
if a>b:
    if a>c:
        print(a)
    else:
        print(c)
elif b>a:
    if b>c:
        print(b)
    else:
        print(c)
'''

#10.waptc second greatest among 3 nos using nested if
'''
a=float(input())
b=float(input())
c=float(input())
if a>b:
    if a>c:
        if b>c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b>c:
        if a>c:
            print(a)
        else:
            print(c)
    else:
        print(b)
'''

#11.wap that determines the movie ticket price based on the age and day
#of the week
'''
Adults(18+):$12(except for Tuesdays:$10)
children(under 18):$8(except for Tuesdays:$6)
seniors(65+):$8(always)
'''
'''
age=float(input('enter age'))
day=input('enter day')
if day.upper() in ('SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY'):
    if day.upper()=='TUESDAY':
        if age>1 and age<18:
            print('6$')
        elif age>=18 and age<65:
            print('10$')
        elif age>=65:
            print('8$')
    else:
        if (age>1 and age<18) or age>=65:
            print('8$')
        elif age>=18 and age<65:
            print('12$')
'''

#12.Leap year checker: wap that determines if a given year is a leap year. A
#leap year is a year divisible by 4, but not by 100 unless it's also div by 400
'''
n=int(input())
if n%4==0:
    if n%100==0:
        if n%400==0:
            print('leap year')
        else:
            print(' not')
    else:
        print('leap year')
else:
    print('not')
'''

#13.Vending machine:create a program for a vending machine that takes product
#code(int ) and amount paid(float) as input. it should check the product price
#(stored in a dictionary) and dispense the product if enough is paid.
#use nested its for different error messages(eg. invalid code, insufficient funds).
'''
n=int(input())
p=float(input())
pro={1:2000,2:1000,3:300}
if n in pro:
    if pro[n]==p:
        print(f'product dispatched')
        pro.pop(n)
    else:
        print('insufficient fund')
else:
    print('invalid code')
'''

#14.Restaurant Discount: wap that calculates a restaurant bill with a discount
#based on the day of the week and part sise:
'''
weekdays(mon-fri),party<4:no discount.
weekdays(mon-fri),party>=4:10% discount.
weekends(sat-sun), any party size: 15% discount
'''
'''
d=input()
ps=int(input())
WEEK=('MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY')
end=('SATURDAY','SUNDAY')
if d.upper() in WEEK:
    if ps<4:
        print('no discount')
    elif ps>=4:
        print('10% discount')
elif d.upper() in end:
    print('15% discount')
else:
    print('invalid input')
'''

#15.shape identifier: design a program that takes 2 inps(len1,len2) and identifiers
#the geometric shape based on the values:
'''
if lenths are equal:square
if one length is twice the other:Rectangle
otherwise:not a square or rectangle
'''
'''
a=float(input())
b=float(input())
c=float(input())
d=float(input())
if a==b and  a==c and a==d:
    print('square')
elif (a==b and c==d) or (a==c and b==d) or (a==d or b==c):
    print('Rectangle')
else:
    print('not a square or rectangle')
'''

#16.waptc the type of a triangle(equilateral,isosceles,scalene)
#usinge nested if
'''
a=float(input())
b=float(input())
c=float(input())

if a==b or a==c:
    if a==b and a==c:
        print('equilateral')
    else:
        print('isosceles')
else:
    print('scalene')
'''
#17.wapt accept any no from 1 to 5 and display that no in word form.if they are
#more than 5 then print no match.
'''
n=int(input())
d={1:'One',2:'Two',3:'Three',4:'Four',5:'Five'}
if 1<=n<=5:
      print(d[n])
else:
    print('no match')
'''





