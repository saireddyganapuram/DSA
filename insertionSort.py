arr = [3,5,1,7,6,9,8]
n = len(arr)
for i in range(0,n):
    j = i
    while(j > 0 and arr[j-1] > arr[j]):
        arr[j-1],arr[j] = arr[j],arr[j-1]
        j -= 1
print(arr)