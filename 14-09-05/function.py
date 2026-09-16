def operations(a,b):
    return a+b, a-b, a*b, a/b


a=int(input("Enter value of a :"))
b=int(input("Enter value of b :"))

addition,subtraction,multiplication, division = operations(a,b)

print("Addition : ", addition)
print("Subtraction : ", subtraction)
print("Multiplication : ", multiplication)
print("Division : ", division)