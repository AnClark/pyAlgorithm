#!/usr/bin/env python3

def QSort(array, LBound, UBound):
    if(LBound >= UBound):
        return
    
    # 首先选定一个基准数
    # 基准数默认为数组第一项
    referer = array[LBound]
    
    # 开始遍历
    j = UBound
    i = LBound
    
    while j > i:
        while not (array[j] < referer) and (j > i):
            j -= 1
        while not (array[i] > referer) and (j > i):
            i += 1
        if i < j:
            buff = array[j]
            array[j] = array[i]
            array[i] = buff
            
        print("i=%d, j=%d" % (i, j))
    
    # 一次重排结束，将基准数归位
    buff = array[j]
    array[j] = referer
    array[LBound] = buff

    print(arr)
    print("===========================")
    
    # 对左右两半部分运行同样的过程
    QSort(array, LBound, j-1)
    QSort(array, j+1, UBound)


import random
arr = [6,1,2,7,9,3,4,5,10,8]
random.shuffle(arr)

print("Original array:" + str(arr))

QSort(arr, 0, 9)

print("Final result:" + str(arr))

    
    
