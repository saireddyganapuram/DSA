arr = [1,2,0,4,3,0,5,0]
i = j = 0
for i in range(len(arr)):
    if(arr[i] != 0):
        arr[i],arr[j] = arr[j],arr[i]
        j += 1
print(arr)