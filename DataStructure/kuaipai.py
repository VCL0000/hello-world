def subSort(arr, low, hight):
    key = arr[low]
    while low < hight:
        while low < hight and arr[hight] >= key:
            hight -= 1
        while low < hight and arr[hight] < key:  # 注1
            arr[hight] = arr[low]
            low += 1
            arr[low] = arr[hight]
    arr[low] = key
    return low


def quickSort(arr, low, hight):
    if i < j:
        key_index = subSort(arr, low, hight)  # 返回的是重合出的指针
        quickSort(arr, low, key_index)  # 左边的再次排序
        quickSort(arr, key_index + 1, hight)  # 右边再次进行排序 指针有变化


'''
注1
双向变换转为单项变换  指针不发生交叉变换
活动指针仍然是hight 将low指针指向的数据赋给hight
 low指针+1
 将higth指针指向low
 活动指针只有hight一个
'''
