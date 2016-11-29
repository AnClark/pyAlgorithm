#!/usr/bin/env python3

def BubbleSort(array):
    len = array.__len__()

    for i in range(len):
        for j in range(i, len):
            if array[i] > array[j]:
                buff = array[i]
                array[i] = array[j]
                array[j] = buff


if __name__ == "__main__":
    import random
    arr = [6,1,2,7,9,3,4,5,10,8]
    random.shuffle(arr)

    print("Original array:" + str(arr))

    BubbleSort(arr)

    print("Final result:" + str(arr))
