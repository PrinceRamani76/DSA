from array import *;

arr = array('i',[1,2,3,4,2,3])

def print_arr(a):
    for i  in range(len(a)):
        print(arr[i])

print("Origial array")
print_arr(arr)

arr.pop()
print("Removed last element using pop() : ")
print_arr(arr)

arr.remove(1)
print("Removed element 1 using remove(1) : ")
print_arr(arr)


arr.extend([6,7])
print("Added elements using extend([6,7]) : ")
print_arr(arr)

arr.append(2)
print("Appended 2 using append(2) : ")
print_arr(arr)

arr.insert(1,12)
print("Inserted elem. at pos. 1 using insert(1,12) : ")
print_arr(arr)

print("Number of times 2 in arr using count(2) : ", arr.count(2))

print("Index of element 3 using index(3)", arr.index(3));

arr.reverse()
print("reversed arrray using reverse()")
print_arr(arr)