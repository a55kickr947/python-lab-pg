def mergeSort(a):
    if (len(a)>1):
        mid=len(a)//2
        l=a[:mid]
        r=a[mid:]
        mergeSort(l)
        mergeSort(r)
        i=j=k=0
        
        while i<len(l) and j<len(r):
            if l[i]<=r[j]:
                a[k]=l[i]
                i+=1
                k+=1
            else:
                a[k]=r[j]
                j+=1
                k+=1
                
        while i<len(l):
            a[k]=l[i]
            i+=1
            k+=1
            
        while j<len(r):
            a[k]=r[j]
            j+=1
            k+=1
            
def PrintList(a):
    for i in range(len(a)):
        print(a[i],end=" ")
    print()
    
if __name__=="__main__":
    a=[12,11,9,8,16,4]
    print("given array is:")
    PrintList(a)
    mergeSort(a)
    print("\nsorted array is:")
    PrintList(a)
    
            
