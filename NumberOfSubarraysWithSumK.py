#this code works for all elements including negatives

def longestSubarray(arr, k):
    n = len(arr)
    sum = 0
    res = 0
    dict1 = {}

    for i in range(n):
        sum += arr[i]

        if sum == k:
            res += 1  

        rem = sum - k
        if rem in dict1:
            res += dict1[rem] 

        if sum in dict1:
            dict1[sum] += 1
        else:
            dict1[sum] = 1

    return res


arr = [1,1,1]
k = 2
result = longestSubarray(arr,k)
print(result)

                
                
            
        
    
