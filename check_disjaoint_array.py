list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
flag=True
for i in list1:
    if(i in list2):
        flag=False
if(flag==False):
    print("array is not disjoint")
else:
    print("array is disjoint")
