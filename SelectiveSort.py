#!/usr/bin/env python3
"""
参照了太阳落雨的选择排序教程
"""
def SelectiveSort(array):
    len = array.__len__()
    
    
    # 遍历数组的各项
    for i in range(len - 1):

        MIN_index = i
        
        # 找出最小的数之索引
        for j in range(i + 1, len):
            if array[j] < array[MIN_index]:
                MIN_index = j

        # 与第i项互换
        buff = array[MIN_index]
        array[MIN_index] = array[i]
        array[i] = buff



if __name__ == "__main__":
    
    import random
    
    arr = [9,2,6,4,7,3,8,1,10,5]
    random.shuffle(arr)

    print("Original Array:" + str(arr))

    SelectiveSort(arr)

    print("Final Array:" + str(arr))
    
            
        
