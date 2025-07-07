arr = [3,5,1,7,8,6,9]
n = len(arr)
for i in range(0,n):
    didSwaps = 0
    for j in range(0,n-i-1):
        if(arr[j] > arr[j+1]):
            arr[j],arr[j+1] = arr[j+1],arr[j]
    if(didSwaps == 0):
        break
print(arr)