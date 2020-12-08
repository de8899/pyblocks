# play wth strings using %strings

ns = input("give me some a number from 1 to 10: ")
num1 = int("%s" % ns)
num2 = int("%s%s" % (ns,ns))
print("single and pair of these put together are ")
print(str(num1) + str(num2))
print("added, the two are: ")
print(num1+num2)


