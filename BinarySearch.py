#!/usr/bin/env python3
import random

def BinarySearch(array, keynumber, LBound, UBound):

    if LBound <= UBound:
        
        mid_index = (UBound + LBound) // 2
        print(mid_index)

        if keynumber == array[mid_index]:
            return mid_index

        # 注意，如果在调用递归函数的过程中不使用这个return语句，
        # 就没有办法结束递归过程！
        # 不要和快速排序算法搞混了。。。。。。

        # 最后的结果会随着递归的返回，被层层带出来。实时打印输出mid_index的值就知道了。
        
        elif keynumber > array[mid_index]:
            return BinarySearch(array, keynumber, mid_index+1, UBound)
            
        elif keynumber < array[mid_index]:
            return BinarySearch(array, keynumber, LBound, mid_index-1)
        
    else:
        return -1
        


if __name__ == "__main__":
    lst = [random.randint(1,100) for x in range(1,10)]

    print("Current List:" + str(lst))

    while True:
        key = int(input("Input a key number:"))

        result = BinarySearch(lst, key, 0, len(lst)-1)

        if result > -1:
            print("Found! At Index %d \n" % result)
        else:
            print("Not Found! \n")

        
