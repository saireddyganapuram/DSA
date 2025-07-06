arr = [4,2,1,5,3]
n = len(arr)
i = 0
while(i < n):
    correct = arr[i] - 1
    if(arr[i] != arr[correct]):
        arr[i],arr[correct] = arr[correct],arr[i]
    else:
        i += 1
print(arr)