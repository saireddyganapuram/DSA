def missinngPositive(arr):
    n = len(arr)
    i = 0
    while(i < n):
        current = arr[i] - 1
        if(arr[i] > 0 and arr[i] < n and arr[i] != arr[current]):
            arr[i],arr[current] = arr[current],arr[i]
        else:
            i += 1

    for i in range(n):
        if(arr[i] != i + 1):
            return i + 1
        
    return n

arr = [2,-3,4,1,1,7]
res = missinngPositive(arr)
print(res)