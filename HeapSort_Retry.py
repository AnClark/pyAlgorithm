#!/usr/bin/env python3
"""
    【堆排序 —— Python 实现】
    博客园之圣骑士 和 CSDN之太阳落雨 的教程为我提供了思路
    接着，就是结合自己的探索来编写~~~
"""

"""
===============================================================
    HeapAdjust —— 核心函数，筛选过程（单次堆调整）
---------------------------------------------------------------
    循环迭代地对二叉树进行调整，使二叉树满足堆的性质。
    但是，每次调整都涉及到序列项的交换，使得新的二叉树不满足堆的性质，
    因此需要调用不止一次。
===============================================================
"""
def HeapAdjust(array):

    # 获取序列的最大索引（右边界）
    UBound = len(array) - 1

    """ 【公式】第一个终端节点下标 = 序列长度 // 2.
                    ∴不难推知，最后一个非终端结点下标 = 序列长度 // 2 - 1.
    """
    # 从最后一个非终端节点往前迭代
    i = len(array) // 2 - 1
    while i >= 0:

        # 获取左右儿子节点的下标
        LChild = i * 2 + 1
        RChild = i * 2 + 2

        # 接下来，在父节点和两个儿子节点中选出最大的
        # 注意：限定儿子节点小于右边界，是为了防止出界——多数是右子节点不存在的情况。
        MAX_index = i

        if LChild <= UBound and array[LChild] > array[MAX_index]:     
            MAX_index = LChild
                
        if RChild <= UBound and array[RChild] > array[MAX_index]:
            MAX_index = RChild

        # 若最大者为儿子节点，则使儿子节点上位。否则此代码实为无效
        buff = array[i]
        array[i] = array[MAX_index]
        array[MAX_index] = buff

        # 继续迭代
        i -= 1


"""
===============================================================
    HeapInit —— 媒介函数，维护堆的性质
---------------------------------------------------------------
    通过连续调用单次堆调整函数 HeapAdjust，
    来得到一个完整的、完全符合堆性质的大顶堆。
===============================================================
"""
def HeapInit(array):

    # 根据圣骑士的方法，只需从最后一个非终端结点开始，往前对所有的非终端结点调用核心函数，
    # 就能充分地使整个二叉树满足大顶堆的性质。
    for i in range(len(array) // 2, 0 - 1, -1):
        HeapAdjust(array)


"""
===============================================================
    HeapSort —— 堆排序的入口函数
---------------------------------------------------------------
    只需要把待排序的序列传进来，就可以返回一个排好序的序列。
    在这里，我运用了Python List类型的pop()方法，
    将每次排序过程所得出来的最大数弹出列表，这时只需对剩余项目进行排序即可。
===============================================================
"""
def HeapSort(array):

    # 先建立初始化堆 
    HeapInit(array)

    # 输出序列，最后结果通过该序列传递
    result = []

    # 接下来要迭代整个原序列
    i = len(array) - 1
    
    while i >= 0:

        # 把筛出来的、当前二叉堆的最大数交换到堆底
        buff = array[i]
        array[i] = array[0]
        array[0] = buff

        # 将筛选出来的大数弹出原序列，放入输出序列中
        # 该数被弹出后，就不存在于原序列了。这样不仅避免原址排序定界的繁冗，还充分运用了Python List对象灵活多变的特性（可当做栈来使用）。
        result.insert(0, array.pop())

        # 对新的二叉堆进行维护
        HeapInit(array)

        # 继续迭代
        i -= 1

    # 输出结果
    return result


"""
==================    以 下 是 测 试 部 分    ==================
"""
if __name__ == "__main__":
    from random import randint, shuffle

    # 用列表生成式生成随机测试序列，并打乱顺序
    arr = [randint(1,100) for x in range(1,20)]
    shuffle(arr)
    # 用Python自带的排序方法对序列进行排序，来核对我的算法是否正确
    arr_orig = sorted(arr)

    # 输出原序列
    print("Original array is:" + str(arr))

    # 输出初始化堆
    HeapInit(arr)
    print("Initialized array is:" + str(arr))

    # 启动正式的堆排序过程
    result = HeapSort(arr)
    print("Sorted array is:" + str(result))

    # 核对答案
    if result == arr_orig:
        print("RIGHT!")
    else:
        print("WRONG!")
        
