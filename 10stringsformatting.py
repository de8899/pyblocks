# play wth strings using %strings
# 20201207 - reformatting/cleanup of text input cmds.
# dev2 updating header

ns = input("Give me some a number from 1 to 20: ")
num1 = int("%s" % ns)
num2 = int("%s%s" % (ns,ns))
print("Single and pair of these put together are ")
print(str(num1) + str(num2))
print("Added, the two are: ")
print(num1+num2)


