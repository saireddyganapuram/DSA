#this code works for all elements including negatives

def longestSubarray(arr, k):
    n = len(arr)
    sum = 0
    maxLen = 0
    dict1 = {}

    for i in range(n):
        sum += arr[i]
        if sum == k:
            maxLen = i + 1            
        rem = sum - k
        if (rem in dict1):
            maxLen = max(maxLen, i - dict1[sum - k])
        if sum not in dict1:
            dict1[sum] = i

    return maxLen

arr = [10,5,2,7,1,-10]
k = 15
result = longestSubarray(arr,k)
print(result)

                
                
            
        
    
