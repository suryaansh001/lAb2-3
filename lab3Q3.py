a=int(input())
b=int(input())
c=int(input())
if a>=b+c:
    print("no")
elif  b>=c+a :
    print("no")
elif c>=b+a:
    print("no")
else:
    print("yes")


'''could also be done by using 
if a>=b+c or c>=b+a or c>=b+a :
    print("no")
    '''