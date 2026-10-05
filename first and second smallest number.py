lst=[]
n=int(input("enter the size of list :"))
for i in range(n):
    value=int(input("enter the element of list :"))
    lst.append(value)
if not lst:
    print("list is empty")
else:
    small=float("inf")
    second=float("inf")
    for i in lst:
        if i<small:
            second=small
            small=i
        elif i<second and i!=small:
            second=i
    if second==float("inf"):
            print("second smallest element not found")
    else:
        print("smallest element is :",small)
        print("second smallest element is :",second)
