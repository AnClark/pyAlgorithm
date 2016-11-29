import random

arr = []

for i in range(1,20):
    arr.append(random.randint(1,100))

print("Current array is: \n" + str(arr))

min_index = 0
for i in range(len(arr)):
    if arr[i] < arr[min_index]:
        min_index = i

print("Minimum is %d at the index %d" % (arr[min_index], min_index))

print("Official answer is: %d" % min(arr))


    
