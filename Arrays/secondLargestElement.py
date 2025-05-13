def findSecondLargestElement(arr):
    try:
        n = len(arr)
        largest = -1
        secondLargest = -1
        for i in range(n):
            if(arr[i] > largest):
                largest = arr[i]
        for j in range(n):
            if(arr[j]>secondLargest and arr[j]!=largest):
                secondLargest = arr[j]
        return secondLargest
    except Exception as e:
        print(e)
        return
    
print(findSecondLargestElement([7,12,14,78,99]))