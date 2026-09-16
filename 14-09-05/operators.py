'''
3. Operators

1. Perform addition, subtraction, multiplication, and division.
2. Find the remainder and quotient of two numbers.
3. Check whether a number is even or odd.
4. Compare two numbers using relational operators.
5. Demonstrate logical operators (and, or, not).
6. Demonstrate assignment operators (+=, -=, *=, /=).
7. Find the largest of two numbers using comparison operators.

'''

#1
print("#1")
a=10
b=20
print("Addition : ", a+b)
print("Subtraction : ", a-b)
print("Multiplication : ", a*b)
print("Division : ", a/b)

#2
print("#2")
print("remainder : ", a%b, " quotient : ", a/b );

#3
print("#3")
if(a%2 ==0):
    print("Even")
else :
    print("Odd")

#4
print("#4")
print("Relational Operators")
print("a<b : ", a<b)
print("a>b : ", a>b)
print("a<=b : ", a<=b)
print("a>= : ", a>=b)
print("a==b : ", a==b)
print("a!=b : ", a!=b)

#5
print("#5")
print("Logical Operators")
print("a and b : ", a and b)
print("a or b : ", a or b)
print("a not b : ", a is not b)

#6
print("#6")
print("Logical Operators")
a+=5
print("Value of a after a+=5 : ",a)
a-=5
print("Value of a after a-=5 : ",a)
a*=5
print("Value of a after a*=5 : ",a)
a/=5
print("Value of a after a/=5 : ",a)

#7 
print("#7")
print("Largest of a and b")
print("a=", a, " b=",b)

if (a==b):
    print("a and b both are equal")
elif a>b:
    print(a)
else:
    print(b)
