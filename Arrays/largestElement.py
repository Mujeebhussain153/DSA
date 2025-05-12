# Iterative way to find out the largest Number in the array
def largestelement(arr):
    try:
        max_element = arr[0]
        for i in range(1, len(arr)):
            if(arr[i] > max_element):
                max_element = arr[i]
        return max_element
    except Exception as e:
        print(e)
        return

# Recursively finding the Largest Element within the Array
def recursiveLargestElement(arr, idx, max_element=None):
    if(max_element == None):
        max_element = arr[0]
    if(idx == len(arr)-1):
        return max_element
    if(arr[idx] > max_element):
        max_element = arr[idx]
    return recursiveLargestElement(arr, idx+1, max_element)


print(largestelement([198,12,85,144,5]))

print(recursiveLargestElement([198,12,85,199,5], 1))