a = [2,3,6,4,9,10]
first = second = -1
for i in range(len(a)):
    if(a[i] > first):
        second = first
        first = a[i]
    elif(a[i] < first and a[i] > second):
        second = a[i]
print("the second largest element is :",second)