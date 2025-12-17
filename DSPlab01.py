
import math

##date and time
import datetime
now = datetime.datetime.now()
print("current date and time:", now)


##2 reverse first and last name

firstname = input("enter your first name:")
lastname= input("enter your last name:")
u= firstname[::-1]
v=lastname[::-1]
print(u,v)

##3

n=int(input("enter a number:"))
result= n+ int(n**2) +int(n**3)
print("result:", result)

#4 sum of three numbers
a = int(input("enter a number:"))
b = int(input("enter a number:"))
c = int(input("enter a number:"))
if(a==b==c):
    print(3*(a+b+c))
else:
    print(a+b+c)

#5solve (x+y)*(x+Y)


x= int(input("enter a number"))
y= int(input("enter a number"))
result2= (x+y)*(x+y)
print(f"({x}+{y}^2 ={result2})")

#6 compound interest


amount= int(input("enter amount"))
rate=  float(input("enter rate"))
years = float(input("no. of years"))
n= int(input("no. of times the interest compunded yearly"))
interest= amount*(1+(rate/100))**(years*n)
print("compound interest:", round(interest,2))

#7 parse a string

s= input("enter a number")
print("integer", int(s))
print("float", float(s))

#8 sum of first n positive integer

n1= int(input("enter a number:"))
sum=0
for i in range (n1+1):
    sum= sum+i
print( "sum=", sum)

#9sum of digits
n2= int(input("enter a number:"))
sum2=0

while(n2!=0):
    num= n2%10
    sum2= sum2+num
    n2= n2//10
print("sum of digits:", sum2)
    
#10 ASCII

ch= input("enter a character:")
print("ASCII value:", ord(ch))

#11)string number

s2= input("enter a string")
if s2.isnumeric():
     print("string is numeric")
else:
    print("string is not numeric")

#12)recatngle pattern

for i in range(5):
    print("***")

# user input
col = int(input("enter no. of columns"))
rows = int(input("enter no. of rows"))
for i in range(rows):
    for i in range(col):
        print("*", end='')
    print()

#13)

for i in range(2000,3201):
    if(i%7==0 and i%5!=0):
        print(i  , end=',')
#15)
rows1= int(input("enter a number:"))
for i in range(rows1,0,-1):
    for j in range(i):
        print(chr(j+65), end='')
    print()

#15)

c=50
h=30
values= input("enter comma separated avlues:").split(",")
result3=[]
for d in values:
    q= math.sqrt((2*c*int(d))/h)
    result3.append(str(round(q)))
print(",".join(result3))













