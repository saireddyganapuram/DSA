arr = [4,3,8,2,9,5,7]
n = len(arr)
for i in range(0,n-1):
    min = i
    for j in range(i,n):
        if(arr[j] < arr[min]):
            min = j
    arr[i],arr[min] = arr[min],arr[i]
print(arr)