# play wth strings using %strings
# 20201207 - reformatting/cleanup of text input cmds.
# dev2 updating header


ns = input("Give me a number from 1 to 11: ")

try:
    if int(ns) > 11:
        print("Too high. Need a number that is 11 or less")
    else:
        print("shit")
except:
    print("something went wrong")
    print("Let's try " + str(ns))

