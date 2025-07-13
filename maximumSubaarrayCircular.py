def maxSubarray(arr):
    n = len(arr)
    totalSum = 0
    maxSum = arr[0]
    minSum = arr[0]
    currMax = 0
    currMin = 0
    for i in range(n):
        currMax = max(currMax + arr[i],arr[i])
        maxSum = max(maxSum , currMax)

        currMin = min(currMin + arr[i],arr[i])
        minSum = min(minSum,currMin)

        totalSum += arr[i]

    norSum = maxSum
    cirSum = totalSum - minSum

    if(norSum < 0):
        return norSum

    return max(cirSum,norSum)

arr = [8,-8,9,-9,10,-11,12]
res = maxSubarray(arr)
print(res)
