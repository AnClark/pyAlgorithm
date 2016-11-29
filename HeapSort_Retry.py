#!/usr/bin/env python3
"""
    【堆排序 —— Python 实现】
"""
def HeapAdjust(array):

    UBound = len(array) - 1
    
    i = len(array) // 2 - 1
    while i >= 0:
        
        LChild = i * 2 + 1
        RChild = i * 2 + 2

        MAX_index = i


        if LChild <= UBound:
            if array[LChild] > array[MAX_index]:
                MAX_index = LChild
                
        if RChild <= UBound:
            if array[RChild] > array[MAX_index]:
                MAX_index = RChild


        buff = array[i]
        array[i] = array[MAX_index]
        array[MAX_index] = buff

        i -= 1


def HeapInit(array):
    for i in range(len(array) // 2, 0 - 1, -1):
        HeapAdjust(array)

def HeapSort(array):
    
    HeapInit(array)
    
    result = []
    
    i = len(array) - 1
    
    while i >= 0:
        
        buff = array[i]
        array[i] = array[0]
        array[0] = buff
        
        result.insert(0, array.pop())

        HeapInit(array)

        i -= 1

    return result


if __name__ == "__main__":
    from random import randint, shuffle

    arr = []
    
    for i in range(20):
        arr.append(randint(1,100))

#    arr = [60,8,30,40,12,70,10]
#    random.shuffle(arr)

#    arr = [12,8,10]

    arr_orig = sorted(arr)

    print("Original array is:" + str(arr))

    HeapInit(arr)

    print("Initialized array is:" + str(arr))

    result = HeapSort(arr)

    print("Sorted array is:" + str(result))

    if result == arr_orig:
        print("RIGHT!")
    else:
        print("WRONG!")
        
