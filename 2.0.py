
arr = [5,3,6,2,10,-1]


def find_Smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = 1
    print(smallest)
    return (smallest_index)
    

find_Smallest(arr)

# O(n)
