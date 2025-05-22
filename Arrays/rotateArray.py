# Function to Rotate an Array based on the number given
def rotateArrNaiveApproach(nums, d):
    try:
        n = len(nums)
        for i in range(d):
            last = nums[-1]
            for j in range(n-1, 0, -1):
                nums[j]= nums[j-1]
            nums[0] = last
        return nums
    except Exception as e:
        print(e)
        return
    
def rotateArrayDirectApproach(nums, d):
    try:
        n = len(nums)
        # Creating an Empty array that's based on the size of the original Array
        temp =[0]*n
        d %= n
        for i in range(d):
            temp[i] = nums[n-d+i]
        for i in range(n-d):
            temp[i+d] = nums[i]
        return temp
    except Exception as e:
        print(e)
        return
    
print(rotateArrNaiveApproach([1,2,3,4,5], 2))
print(rotateArrayDirectApproach([1,2,3,4,5], 2))
