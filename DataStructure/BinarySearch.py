def BinarySearch(arr, m):
    low = 0
    high = len(arr) - 1
    while (low < high):
        mid = (low + high) // 2  # //为整除
        if arr[mid] > m:
            high = mid - 1
        elif arr[mid] < m:
            low = mid + 1
        else:
            return mid
    return -1  # 不存在返回的
