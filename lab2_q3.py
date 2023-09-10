x=int(input("enter a number"))
y=int(input("enter a number"))
if x<0 or y<0:
    print("invalid input")
elif y%x==0:
    print("yes ")
else:
    print("no")
