def findSecondLargestElement(arr):
    try:
        n = len(arr)
        largest = -1
        secondLargest = -1
        for i in range(n):
            if(arr[i] > largest):
                secondlargest = largest
                largest = arr[i]
            elif(arr[i] > secondlargest and arr[i]!=largest):
                secondlargest = arr[i]
        return secondlargest
    except Exception as e:
        print(e)
        return
    
print(findSecondLargestElement([105,7,12,14,78,99]))