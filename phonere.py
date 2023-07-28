import re
n=input("enter a phone number:")
p1=re.compile(r'\ddd\-\ddd\-\dddd')
p2=p1.search('txt')
print(p2.group())
