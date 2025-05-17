# This Function is to check whether the array is sorted or not
def isSorted(nums):
    try:
        largest = -1
        n = len(nums)
        for i in range(n):
            if(nums[i] > largest):
                largest = nums[i]
        return largest == nums[-1]
    except Exception as e:
        print(e)
        return

print(isSorted([20, 20, 78, 98, 99, 97]))