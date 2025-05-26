def selectionSort(nums):
    try:
        n = len(nums)
        for i in range(n):
            min_index = i
            for j in range(i+1, n):
                if(nums[j] < nums[min_index]):
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums
    except Exception as e:
        print(e)
        return
    
print(selectionSort([4,5,1,12,9]))
print(selectionSort([4,13,78,0,9]))