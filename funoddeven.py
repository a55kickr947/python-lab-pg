def oddeven(x):
    if(x%2==0):
        return 1
    else:
        return -1
a=int(input("a="))
b=oddeven(a)
if(b==1):
    print("even")
else:
    print("odd")
