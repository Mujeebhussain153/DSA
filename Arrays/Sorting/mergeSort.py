def mergeSort(arr):
    try:
        if(len(arr) <=1):
            return arr
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        return merge(left, right)
    except Exception as e:
        print(e)
        return

# Merging the Elements based on the max and min of the elements
def merge(left, right):
    try:
        merged = []
        i, j = 0, 0
        while(i< len(left) and j < len(right)):
            if(left[i] <= right[j]):
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        merged+=left[i:]
        merged+=right[j:]
        return merged
    except Exception as e:
        print(e)
        return

print(mergeSort([5,2,4,3,1]))