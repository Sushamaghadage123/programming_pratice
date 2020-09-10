array=list(map(int,input().split()))
sum=0
for i in array:
    sum+=i
average=sum/len(array)
print("sum of array element:",sum,"average of array element:",average)
