def zerosToEnd(nums):
    try:
        n = len(nums)
        temp = []
        for i in range(n):
            if(nums[i]!=0):
                temp.append(nums[i])
        for i in range(n):
            if(nums[i] == 0):
                temp.append(nums[i])
        return temp
    except Exception as e:
        print(e)
        return
    
def singleTraversalApproch(nums):
    try:
        n = len(nums)
        counter = 0
        for i in range(n):
            if(nums[i] != 0):
                nums[i],  nums[counter] = nums[counter], nums[i]
                counter+=1
        return nums
    except Exception as e:
        print(e)
        return

print(zerosToEnd( [10, 20, 30]))
print(singleTraversalApproch([1, 2, 0, 4, 3, 0, 5, 0]))