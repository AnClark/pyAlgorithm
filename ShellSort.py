#!/usr/bin/env python3
"""
【希尔排序——每次简单插入排序均为自后向前查找】
本希尔排序算法参考太阳落雨的希尔排序讲解，以及博客园 kkun 的简单插入排序讲解
"""

def ShellSort(array, gap):

    if gap < 1:
        return

    for i in range(gap, len(array)):

        current = array[i]
        
        j = i
        
        while (array[j - gap] > current) and (j > 0):
            array[j] = array[j - gap]
            j -= gap

        array[j] = current

    ShellSort(array, gap // 2)



if __name__ == "__main__":
    import random
    arr = [9,7,2,6,1,10,8,3,4,5]
    random.shuffle(arr)

    print("Original array:" + str(arr))

    ShellSort(arr, len(arr) // 2)

    print("Final array:" + str(arr))
