# Nested Loop Approach
def findLeaderElements(nums):
    try:
        n = len(nums)
        leader_ele = []
        for i in range(n):
            for j in range(i+1, n):
                if(nums[i] < nums[j]):
                    break
            else:
                leader_ele.append(nums[i])
        return leader_ele
    except Exception as e:
        print(e)
        return

# Single Loop Approach
def findLeaders2(nums):
    try:
        n = len(nums)
        leader_ele = nums[-1]
        leader_elements_list = [leader_ele]
        for i in range(n-2, -1, -1):
            if(nums[i] > leader_ele):
                leader_elements_list.append(nums[i])
                leader_ele = nums[i]
        return leader_elements_list[::-1]
    except Exception as e:
        print(e)
        return


print(findLeaderElements([12, 14, 7, 10, 5, 2]))
print(findLeaderElements([12, 14, 7, 10, 11, 2]))

print(findLeaders2([12, 14, 7, 10, 5, 2]))
print(findLeaders2([12, 14, 7, 10, 11, 2]))