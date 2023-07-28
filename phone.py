def phone(num):
    if(len(num)!=12):
        return print("it is not a valid phone number")
    for i in range(0,3):
        if not num[i].isdecimal():
            return print("not a phone number")
    if num[3] and num[7]!="-":
        return print("not a phone number")
    for i in range(4,7):
        if not num[i].isdecimal():
            return print("not a phone number")
    for i in range(8,12):
        if not num[i].isdecimal():
            return print("not a phone number")
    return print("it is a valid phone number")
num=input("enter a phone number:")
phone(num)
