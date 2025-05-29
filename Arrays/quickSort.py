def quickSort(nums):
    try:
        if(len(nums) <= 1):
            return nums
        # Getting the pivot element (Center Element)
        pivot = nums[len(nums)//2]
        # Getting the elements that are lesser than the pivot element
        left = [i for i in nums if i < pivot]
        middle = [i for i in nums if i==pivot]
        right = [i for i in nums if i>pivot]
        # combining all the parts together recursively
        return quickSort(left) + middle + quickSort(right)
    except Exception as e:
        print(e)
        return
    
print(quickSort([5, 1, 2, 4, 3]))