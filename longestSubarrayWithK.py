#this code only works for if the array has zeros and positives

def longestSubarray(arr,k):
    n = len(arr)
    left = 0
    right = 0
    maxLen = 0
    sum = arr[0]
    while(right < n):
        while(left <= right and sum > k):
            sum -= arr[left]
            left += 1
        if(sum == k):
            maxLen = max(maxLen,right-left + 1)
        right += 1
        if(right < n):
            sum += arr[right]
        
    return maxLen

arr = [1,2,3,0,0,1,1,1,3,3]
k = 3
result = longestSubarray(arr,k)
print(result)