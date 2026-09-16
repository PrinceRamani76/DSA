'''
5. Loops

1. Print numbers from 1 to 10 using a for loop.
2. Print numbers from 10 to 1 using a while loop.
3. Print the multiplication table of a number.
4. Find the sum of numbers from 1 to n.
5. Find the factorial of a number.
6. Print all even numbers between 1 and 100.
7. Reverse a number using a loop.
8. Count the digits of a number.
9. Check whether a number is prime.
10. Print Fibonacci series up to n terms.
'''
import math;

#1
print("#1")
print("1 to 10 using for")
for i in range(1,11):
    print(i)

#2
print("#2")
print("10 to 1 using for")
a=10
while (a >0):
    print(a)
    a-=1

#3
print("#3")
n= int(input("Enter num to print table : "))
for i in range(1,11):
    print(n, " x ", i, " = ", n*i)

#4
print("#4")
p= int(input("Enter num to print table sum till that number : "))
sum=0
for i in range(1,p):
    sum+=i
    
print("Sum from 1 to ", p ,"is = ",sum)

#5 
print("#5")
fact = 1;
f= int(input("Enter num to find factorial of that number : "))

while(f>0):
    fact*=f
    f-=1
    
#6 
print("#6")
print("All even numbers between 1..100")
for i in range(1,100):
    if(i%2==0):
        print(i)
    
    
#7
print("#7")
num= int(input("Enter num to Reverse it : "))
no=0;
while(num>0):
    temp=num%10
    no = int(no*10+temp)
    num = (num-temp)/10

print(no)


#8
print("#8")
num= int(input("Enter num to count digits : "))
digits=0;

while(num>0):
    temp=num%10
    digits+=1
    num = (num-temp)/10

print(digits)

#9
print("#9")
num= int(input("Enter num to check whether it is prime or not : "))
is_prime = True

if num <=1:
    is_prime = False
else:
    for i in range(2, int(math.ceil(math.sqrt(num)))+1):
        if num%i == 0:
            is_prime = False

if is_prime : 
    print(num," is prime number")
else:
    print(num," is not a prime number")

#10
print("#10")
num= int(input("Enter num to print Fibonacci numbers : "))

prev=0
next=1

for i in range(0,
num):
    print(prev)
    temp=next
    next = prev+next
    prev =  temp
    
  
  

