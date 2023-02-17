# Python drills - practice the basics - use W3 schools python examples for reference. 

# Create a list, tuple, set, and dictionary. List is same as array.
list1=["mary","ray","bob"]
tuple1=("this","tupler","thing")
set1={"car","dog","toy"}
dict1={"Los Aangeles":"LA","New York":"NY"}

# Do loop over one of the above iterables
for i in tuple1:
    import time
    #sleep=time.sleep(1)
    #sleep
    print(i)

# While loop over one of the above iterables
n = 0
while n<3:
    print(list1[n])
    n+=1

# If statement on iterable with try/except
a = 10
b = 20

ns = input("Give me a number from 1 to 11: ")

try:
    if int(ns) > 11:
        print("Too high. Need a number that is 11 or less")
    else:
        print("Let's try " + str(ns))
        try:
            a = 1//0
            print(a)
        except:
            print("cannot divide by 0")

    # Add to the list using input()
    print("here's set1:")
    print(set1)

    print("Now lets add to it. Type a name:")
    inputData = input()
    set1.add(inputData)
    print("now here's set1:")
    print(set1)

    # Remove an item from the list
    print("Now lets remove dog")
    set1.remove('dog')
    print("now here's set1 again:")
    print(set1)

except:
    print("something went wrong")
    

# Empty the list

# Read the second item of the dictionary

# Slice an iterable showing items 2 and 3 only

# Find two built in functions at python.org and demonstrate it's use

# Create a class (will be parent class) with two props, create one object using the class

# Create a child class that inherits the parent class above

# Create a module and reference it in a script

# Create a lambda function

# find the data type of a variable (type())


