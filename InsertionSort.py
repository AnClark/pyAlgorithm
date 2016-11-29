#!/usr/bin/env python3
"""
【插入排序——自后向前查找】
本插入排序程序参照了博客园 kkun 的 Java 代码
http://www.cnblogs.com/kkun/archive/2011/11/23/2260265.html
"""

def InsertSort(array):

    for i in range(1, len(array)):
        
        current = array[i]

        j = i

        # 查找和移动会同时进行
        # 查找的是插入点，移动的是比当前项大的项。移动是为了腾出插入的空间
        while (array[j - 1] > current) and (j > 0):
            array[j] = array[j - 1]    
            j -= 1
            
        array[j] = current

    return array

            
if __name__ == "__main__":       
    import random
    arr = [9,7,2,6,1,10,8,3,4,5]
    random.shuffle(arr)

    print("Original array:" + str(arr))

    InsertSort(arr)

    print("Final array:" + str(arr))


