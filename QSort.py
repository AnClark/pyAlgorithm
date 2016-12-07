#!/usr/bin/env python3
"""
【快速排序】
我心目中的排序算法之王，C++标准库自带排序函数
"""
def QSort(array, LBound, UBound):
    # 递归终止条件
    if(LBound >= UBound):
        return
    
    # 首先选定一个基准数
    # 基准数默认为数组第一项
    referer = array[LBound]
    
    # 开始遍历

    # 划定两个“哨兵”的起始位置
    j = UBound
    i = LBound
    
    while j > i:
        # 右哨兵自右向左遍历，找寻小于基准数的数组项
        while not (array[j] < referer) and (j > i):
            j -= 1
        # 左哨兵自左向右遍历，找寻大于基准数的数组项
        while not (array[i] > referer) and (j > i):
            i += 1
        # 将找到的两项交换顺序
        if i < j:
            buff = array[j]
            array[j] = array[i]
            array[i] = buff
            
    
    # 一次重排结束，将基准数归位
    buff = array[j]
    array[j] = referer
    array[LBound] = buff

    
    # 对左右两半部分运行同样的过程
    QSort(array, LBound, j-1)
    QSort(array, j+1, UBound)


import random
arr = [random.randint(1,1000) for x in range(1,1000)]
random.shuffle(arr)

print("Original array:" + str(arr))

QSort(arr, 0, len(arr)-1)

print("Final result:" + str(arr))

arr_orig = sorted(arr)
if arr_orig == arr:
    print("################ RIGHT! ################")
else:
    print("################ WRONG! ################")
    
