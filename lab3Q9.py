bs=int(input())
hra=0.2*bs
ta=0.05*bs
da=0.1*bs
gs=bs+hra+ta+da
print("gross salry is :",gs)
l=100000
if gs<3*l:
    print("0%")
elif gs>=3*l and gs<10*l:
    print("10%")
elif gs>=10*l and gs<25*l:
    print("20%")
else:
    print("30%")