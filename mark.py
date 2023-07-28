def student(*args):
    tot=0
    for i in args:
        tot=tot+i
    return tot,(tot/len(args))
print("total, percentage=",student(12,23,56,32,14,65))

