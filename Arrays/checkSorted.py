# This Function is to check whether the array is sorted in ascending Order or not
def isSorted(nums):
    try:
        n = len(nums)
        for i in range(1, n):
            if(nums[i-1] > nums[i]):
                return False
        return True
    except Exception as e:
        print(e)
        return

print(isSorted([2, 11, 45, 99, 154]))
print(isSorted([2, 78, 45, 99, 154]))