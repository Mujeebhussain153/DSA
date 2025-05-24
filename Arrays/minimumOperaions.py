def minKOperations(nums, k):
    try:
        operations = 0
        largest_number = -1
        n = len(nums)
        for i in range(n):
            if(nums[i] > largest_number):
                largest_number = nums[i]
        for i in range(n):
            while(nums[i] != largest_number):
                nums[i]+=k
                operations+=1
                if(nums[i] > largest_number):
                    return -1
        return operations
    except Exception as e:
        print(e)
        return
    
def minKOperationsSingle(nums, k):
    try:
        max_ele = max(nums)
        counter = 0
        n = len(nums)
        for i in range(n):
            if((max_ele-nums[i])%k !=0):
                return -1
            else:
                counter+=(max_ele-nums[i])//k
        return counter
    except Exception as e:
        print(e)
        return
    
print(minKOperations([4, 7, 19, 16], 3))
print(minKOperationsSingle([4, 7, 19, 16], 3))
# If any element is smaller than the largest element it should be incremented by k until it becomes equal yo larger element
# As you increment the number by k increase the number of operations by 1
