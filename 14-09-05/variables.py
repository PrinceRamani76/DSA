'''1. Variables

1. Create variables to store name, age, and city and display them.
2. Swap the values of two variables.
3. Calculate the area of a rectangle using variables.
4. Calculate simple interest using variables.
5. Convert Celsius temperature to Fahrenheit.'''

#1
print("#1")
name="Someone"
age=20
city="Rajkot"

print("Name : ",name)
print("Age : ",age)
print("City : ",city)


#2 
print("#2")
a=10
b=20

print("Value of a before swap : ",a)

print("Value of b before swap : ",b)
temp=b
b=a
a=b

print("Value of a after swap : ",a)
print("Value of b after swap : ",b)

#3
print("#3")
print("Calculate area of rectangle->")
height= int(input("Enter height: "))
width= int(input("Enter width: "))

print("Area of rectangle = ", height*width)

#4
print("#4")
p= int(input("Enter principal: "))
r= int(input("Enter rate of interest: "))
n= int(input("Enter duration(n): "))

si= (p*r*n)/100
print("Simple interest : ",si)

#5
print("#5")
cel=int(input("Enter celsius : "))
f= (cel * 9/5) +32
print("fahrenheit of : ",f)
