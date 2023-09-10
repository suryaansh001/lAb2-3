x=int(input())
if x%400==0:
    print("yes")
elif x%4==0 and x%100!=0:
    print("yes")
else:
    print("no")