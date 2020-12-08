import datetime
funs = dir(datetime)


for x in funs:
    print(x)
    
print((datetime.datetime.now()).strftime("%Y-%m-%d"))