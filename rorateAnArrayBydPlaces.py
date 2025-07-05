def reverse(arr,start,end):
    while(start < end):
        arr[start],arr[end] = arr[end],arr[start]
        start += 1
        end -= 1

arr = [1,2,3,4,5,6]
n = len(arr)
d = 3
reverse(arr,0,d-1)
reverse(arr,d,n-1)
reverse(arr,0,n-1)

print(arr)