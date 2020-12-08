import os
import time
import array


array1 = ["w42","dc41","w43"]

for i in array1:
 print(i + " ------")

print(array1[1] + " <- This is the 2nd member of the array")

val1 = input("Add a server name: ")
print("You typed: " + val1)
array1.append(val1)
print("Here's the array now: ")
print(array1)





