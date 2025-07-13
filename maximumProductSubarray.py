def maxProduct(arr):
    n = len(arr)
    leftPro = 1
    rightPro = 1
    maxPro = float("-inf")
    for i in range(n):
        leftPro *= arr[i]
        rightPro *= arr[n-i-1]
        maxPro = max(maxPro,leftPro,rightPro)

        if(leftPro == 0):
            leftPro = 1
        if(rightPro == 0):
            rightPro = 1
    return maxPro

arr = [2,3,-2,4]
res = maxProduct(arr)
print(res)