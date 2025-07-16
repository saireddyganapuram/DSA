def minimizeHeights(arr , k):
    arr.sort()
    n = len(arr)
    res = arr[n-1] - arr[0]
    for i in range(1,n):
        if(arr[i] - k < 0):
            continue
        minH = min(arr[0] + k,arr[i] - k)
        maxH = max(arr[i-1] + k,arr[n-1] - k)
        res = min(res,maxH - minH)
    return res 

arr = [3,9,12,16,20]
k = 3
res = minimizeHeights(arr,k)
print(res)
