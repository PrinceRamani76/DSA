'''
4. Conditions

1. Check whether a number is positive, negative, or zero.
2. Check whether a person is eligible to vote.
3. Find the largest of three numbers.
4. Check whether a year is a leap year.
5. Create a grade system based on marks.
6. Check whether a number is divisible by 5 and 11.
7. Create a simple calculator using if-elif-else
'''

#1
print("#1")
a=int(input("Enter number to check pos , neg or zero : "))

if(a>0):
    print("Postive")
elif(a<0):
    print("Negative")
else:
    print("Zero")


#2
print("#2")
age=int(input("Enter age: "))

if(age>18):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")


#3
print("#3")
a=int(input("Enter number 1 : "))
b=int(input("Enter number 2 : "))
c=int(input("Enter number 3 : "))

if(a>b and a>c):
    print(a," is largest.")
elif b>a and b>c:
     print(b," is largest.")
else:
     print(c," is largest.")


#4
print("#4")
year= int(input("Enter year to find whether it's an leap year or not : "))

if( year %4 == 0 or  year % 400 ==0 ):
    print(year , " is leap year.")
else:
    print(year, " is not a leap year.")


#5
print("#5")
c=int(input("Enter marks of c : "))
cpp=int(input("Enter marks of cpp : "))
per=((c+cpp)*100)/200
if (per >90 ):
    print("Grade : A+")
elif (per>80):
    print("Grade : A")
elif (per>70):
    print("Grade : B")
elif (per>60):
    print("Grade : C")
elif (per>50):
    print("Grade : D")
else:
    print("Grade : F")


#6 
print("#6")
num=int(input("Enter num to check whether its divisable by 5 or 11: "))

if (num%5 == 0):
    print(num," is divisable by 5.")
elif(num%11 == 0):
        print(num," is divisable by 11.")
else:
        print(num,"is not divisable by 5 or 11.")


#7
print("7")
num=int(input("Enter 1 for add, 2 for sub, 3 for division, 4 for multiplication : "))
a=int(input("Enter num1 : "))
b=int(input("Enter num2 : "))

if(num ==1):
    print("Addition : ",  a+b)
elif(num==2):
     print("Subtraction : ",  a-b)
elif(num==3):
     print("Division: ",  a/b)
elif(num==4):
     print("Multiplication : ",  a*b)
else:
    print("Invalid choice.")

