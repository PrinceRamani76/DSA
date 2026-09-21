# 1.	Write a function to print "Hello, World!".
# 2.	Write a function that takes a name and prints a greeting.
# 3.	Write a function to add two numbers.
# 4.	Write a function to find the square of a number.
# 5.	Write a function to check whether a number is even or odd.
# 6.	Write a function to find the maximum of two numbers.
# 7.	Write a function to convert Celsius to Fahrenheit.
# 8.	Write a function to calculate the area of a circle.
# 9.	Write a function to calculate the factorial of a number.
# 10.	Write a function to check whether a number is positive, negative, or zero.
# 11.	Write a function to find the maximum of three numbers.
# 12.	Write a function to count vowels in a string.
# 13.	Write a function to reverse a string.
# 14.	Write a function to check whether a string is a palindrome.
# 15.	Write a function to find the sum of all elements in a list.
# 16.	Write a function to find the largest element in a list.
# 17.	Write a function to remove duplicate elements from a list.
# 18.	Write a function to count how many times an element appears in a list.
# 19.	Write a function to check whether a number is prime.
# 20.	Write a function to return all prime numbers between two numbers.
# 21.	Write a function to calculate Fibonacci numbers.
# 22.	Write a function to find the second-largest number in a list.
# 23.	Write a function to sort a list without using sort().
# 24.	Write a function to merge two lists and remove duplicates.

import math

#1
print("#1")
def print_hello_world():
    print("Hello world")

print_hello_world()

#2


print("#2")
def greeting():
    a=input("Enter ur name : ")
    print("Hello ", a)

greeting()

#3
print("#3")
def add_2():
    a=int(input("Enter number 1 to add : "))
    b=int(input("Enter number 2 to add : "))
    print("Addition of ", a , " and ", b , " = ",a+b)

add_2()

#4
print("#4")
def square_of_num():
    a=int(input("Enter number to get square : "))
    print("square of ", a, " = ", a*a)

square_of_num()

#5

print("#5")
def odd_even():
    n=int(input("Enter number to check odd or even : "))
    if (n %2 == 0):
        print(n," is even.")
    else:
        print(n," is odd.")

odd_even()

#6


print("#6")
def maximum():
    a=int(input("Enter number 1 to check max : "))
    b=int(input("Enter number 2 to check max : "))
    if a>b:
        print(a," is greater than ",b)
    elif b>a:
        print(b, "is greater than ",a)
    else:
        print(a , " and ",b ," both are equal.")

maximum()

#7

print("#7")
def far():
    cel=int(input("Enter celsius : "))
    f= (cel * 9/5) +32
    print("fahrenheit of : ",f)
far()

#8


print("#8")
def area_of_circle():
    r=float(input("Enter radius to find aoc : "))
    print("aoc : ", 3.14*(r*r))

area_of_circle()
#9

print("#9")
def factorial():
    num=int(input("Enter number to print factorial : "))
    fact=1
    while(num>0):
        fact*=num
        num-=1
        
    print("factorial : ", fact);
    
factorial()

#10
print("#10")
def pos_neg_eq():
    a=int(input("Enter number to check pos , neg or zero : "))

    if(a>0):
        print("Positive")
    elif(a<0):
       print("Negative")
    else:
       print("Zero")


#11

print("#11")
def max_3():
    
    a=int(input("Enter number 1 : "))
    b=int(input("Enter number 2 : "))
    c=int(input("Enter number 3 : "))
    
    if(a>b and a>c):
        print(a," is largest.")
    elif b>a and b>c:
         print(b," is largest.")
    else:
         print(c," is largest.")

max_3()

#12

print("#12")
def count_vowels():
    a = input("Enter string to count vowels : ").lower()
    b = ['a','e','i','o','u']
    count=0
    for i in range(len(a)):
        if (a[i] in b):
            count+=1
            
    print("Number of vowels : ",count)
    
count_vowels()

#13

print("#13")
def reverse_string():
     a = input("Enter string to reverse it: ")
     print(a[::-1])

reverse_string()
        
#14


print("#14")
def palindrome():
    a = input("Enter string to find whether it palindrome or not : ")
    
    if a == a[::-1]: 
        print("Palindrome.")
    else:
        print("Not Palindrome")
        
palindrome()

#15


print("#15")
def sum_of_list():
    a=[1,2,3,4,5]
    sum_of_list=0
    for i in a:
        sum_of_list+=i
        
    print("Sum of list : ", sum_of_list)
    

sum_of_list()

#16

print("#16")
def largest_in_list():
    a=[1,2,3,4,5]
    
    print("Largest in list : ",max(a))

largest_in_list()

#17

print("#17")
def remove_dup():
     a=[1,2,3,4,5,5]
     print("list : ", a)
     
     b = list(set(a))
     print("Removed duplicates : ",b)

remove_dup()

#18


print("#18")
def count_elems():
    a =[1,2,3,4,5,6,4,3]
    b={}
    
    print("Count of all elemets in list")

    for i in a:
        if  i in b: 
            b[i] = b.get(i)+1
        else:
            b[i] = 1
            
    print(b)
    
count_elems()

#19


print("#19")
def prime_or_not():
    num = int(input("Enter num to check whether it is prime or not : "))
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


prime_or_not()
#20

print("#20")
def prime_or_not():
    a= int(input("Enter start number to get prime from range : "))
    b= int(input("Enter end number to get prime from range : "))
    count = []

    if(a>=b):
        print("Invalid range")
        return
    
    for i in  range(a,b):
        is_prime = True
        if i <=1:
            is_prime = False
        else:
            for j in range(2, int(math.ceil(math.sqrt(i)))+1):
                if i%j == 0:
                    is_prime = False

            if is_prime : 
                count.append(i)

    print(count)

prime_or_not()

#21
print("#21")
def fibonacci():
    num= int(input("Enter num to print Fibonacci numbers : "))

    prev=0
    next_num=1

    for _ in range(0,num):
        print(prev)
        temp=next_num
        next_num = prev+next_num
        prev =  temp
        
fibonacci()
    
