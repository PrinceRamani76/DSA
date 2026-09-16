'''2. Data Types

1. Demonstrate int, float, str, bool, and complex.
2. Accept two numbers and display their data types.
3. Convert a string number into an integer and float.
4. Find the length of a string.
5. Create a list, tuple, set, and dictionary and display their types.
'''

#1
print("#1")
a=10
print("int : ", a)
a=1.10
print("float : ", a)
a="Hello"
print("string : ", a)
a=True
print("bool : ", a)
a=10.2j
print("complex : ", a)


#2
print("#2")
a=input("Enter number 1 : ")
b=input("Enter number 2 : ")

print("Type of number 1",type(a))
print("Type of number 2",type(b))


#3
print("#3")
str_var = "10"
int_var = int(str_var)
float_var = float(str_var)

print("String : ", str_var)
print("String to int : ", int_var)
print("String to float : ", float_var)

#4 
print("#4")
print("Length of ", str_var, " : " , len(str_var))

#5
print("#5")
list_var = [1,2,3,4];
tuple_var= (1,2,3,4);
dictionary_var = {
    "name" : "Someone",
    "age" : 20
}

print("Type of list_var : ",type(list_var))
print("Type of  tuple_var : ",type(tuple_var))
print("Type of dictionary_var : ",type(dictionary_var))

