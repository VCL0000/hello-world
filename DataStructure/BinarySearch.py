def BinarySearch(arr, m):
    low = 0
    high = len(arr) - 1
    while (low < high):
        mid = (low + high) // 2
        if arr[mid] > m:
            high = mid - 1
        elif arr[mid] < m:
            low = mid + 1
        else:
            return mid
    return -1

# arr = [1, 2, 3, 5, 7, 8, 9]
