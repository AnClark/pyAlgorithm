#!/usr/bin/env python3
"""
递归二分查找算法
参考自话别深秋的CSDN博客
http://blog.csdn.net/q3498233/article/details/4419285
"""
import random

def BinarySearch(array, keynumber, LBound, UBound):

    if LBound <= UBound:
        
        mid_index = (UBound + LBound) // 2
        # print(mid_index)

        if array[mid_index] == keynumber:
            return mid_index
        
        elif array[mid_index] < keynumber:
            return BinarySearch(array, keynumber, mid_index+1, UBound)
            
        elif array[mid_index] > keynumber:
            return BinarySearch(array, keynumber, LBound, mid_index-1)
        
    else:
        return -1
        




def GenerateSortedRandomList(num_count):
    lst = []
    for i in range(num_count):
        lst.append(random.randint(1,100))
    lst.sort()
    return lst
    

if __name__ == "__main__":
    lst = GenerateSortedRandomList(7)

    print("Current List:" + str(lst))

    while True:
        key = int(input("Input a key number:"))

        result = BinarySearch(lst, key, 0, 7-1)
        print(result)

        if result > -1:
            print("Found! At Index %d \n" % result)
        else:
            print("Not Found! \n")

        
