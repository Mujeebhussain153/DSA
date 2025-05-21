# Function to Reverse an Array Using Two pointers
def reverseArr(nums):
    try:
        n = len(nums)
        l = 0
        r = len(nums)-1
        while(l<r):
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        return nums
    except Exception as e:
        print(e)
        return

def recurReverseArr(nums):
    if(not nums):
        return []
    return [nums[-1]]+recurReverseArr(nums[:-1])

print(reverseArr([1,2,2,3,3,4,5]))
print(recurReverseArr([1,2,2,3,3,4,5]))