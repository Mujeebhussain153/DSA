def quickSort(nums):
    try:
        if(not nums):
            return []
        # finding the pivot
        pivot = nums[len(nums)//2]
        # getting the elements that are lower than the pivot element
        left = [i for i in nums if i<pivot]
        # getting the elements that are equal to the pivot element
        middle = [i for i in nums if i==pivot]
        # getting the elements that are higher than the pivot element
        right = [i for i in nums if i>pivot]
        return quickSort(left) + middle +quickSort(right)
    except Exception as e:
        print(e)
        return

def binarySearch(nums, target):
    try:
        nums = quickSort(nums)
        l = 0
        r = len(nums)-1
        while(l<=r):
            mid = (l+r)//2
            if(target == nums[mid]):
                return mid
            elif(nums[mid] > target):
                r = mid -1
            elif(nums[mid] < target):
                l = mid+1
        return -1
    except Exception as e:
        print(e)
        return
    
print(quickSort([7,14,5,12,9,15,18]))
print(binarySearch([7,14,5,12,9,15,18], 9))