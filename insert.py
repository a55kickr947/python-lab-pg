def insertSort(a):
    for i in range(1,len(a)):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
a=[12,11,5,13,6]
insertSort(a)
for i in range(len(a)):
    print("%d,"%a[i],end="")
