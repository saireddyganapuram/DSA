def partition(arr, low, high):
    pivot = arr[low]
    i = low 
    j = high

    while i<j:
        while i <= high and arr[i] <= pivot:
            i += 1
        while j >= low and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j

def quickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quickSort(arr, low, p - 1)
        quickSort(arr, p + 1, high)

arr = [4, 2, 1, 3, 6, 5, 8, 9]
quickSort(arr, 0, len(arr) - 1)
print(arr)
