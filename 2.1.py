arr = [3,6,1,1,1,-1]

def find_Smallest2(arr):
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] < arr[j]:
                min_el = arr[i]
    return (min_el)


print(find_Smallest2(arr))


# O(n^2)
