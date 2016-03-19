def sub_sort(arr, low, high):
    key = arr[low]  # 取low处作为基准数据
    while low < high:
        while low < high and arr[high] >= key:
            high -= 1
        while low < high and arr[high] < key:  # 注1
            arr[low] = arr[high]
            low += 1
            arr[high] = arr[low]
    arr[low] = key  # 注3
    return low


def quick_sort(arr, low, high):  # 注2
    if low < high:
        key_index = sub_sort(arr, low, high)  # 返回的是重合出的指针
        quick_sort(arr, low, key_index)  # 左边的再次排序
        quick_sort(arr, key_index + 1, high)  # 右边再次进行排序 指针有变化


'''
注1
双向变换转为单项变换  指针不发生交叉变换
活动指针仍然是high 将low指针指向的数据赋给high
 low指针+1
 将higth指针指向low
 活动指针只有high一个

 注2
 low为0  height为arr.len-1

 注3
 将基准数据移动到low指针
'''

if __name__ == "__main__":
    array = [8, 7, 6, 5, 9, 3, 1]
    print(array)
    quick_sort(array, 0, len(array)-1)
    print(array)
