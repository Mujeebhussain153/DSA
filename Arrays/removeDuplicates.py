# Method to Remove Duplicates from an array if they exist
def removeDuplicates(nums):
    try:
        array_without_duplicates = []
        n = len(nums)
        if(n <=1):
            return nums
        for i in range(n):
            if nums[i] in array_without_duplicates:
                continue
            else:
                array_without_duplicates.append(nums[i])
        return array_without_duplicates
    except Exception as e:
        print(e)
        return
    
print(removeDuplicates([10, 10, 15, 20, 25, 30, 30]))