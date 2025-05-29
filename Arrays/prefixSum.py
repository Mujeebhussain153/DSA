def prefixSum(nums):
    try:
        pre = [0]*len(nums)
        pre[0] = nums[0]
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]+nums[i]
        return pre
    except Exception as e:
        print(e)
        return

print(prefixSum([1,2,3,4,5]))