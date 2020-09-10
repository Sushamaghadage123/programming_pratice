array=list(map(int,input().split()))
array2=list(set(array))
array2.sort()
print("second max element from array",array2[-2])
