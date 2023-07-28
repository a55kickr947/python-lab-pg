a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
if(a<b) and (b<c):
    print(c,'is the greatest')
elif (a<b) and (a>c):
    print(b,'is the greatest')
else:
    print(a,'is the greatest')
    
