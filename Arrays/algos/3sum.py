def threeSum(nums):
    try:
        arr = sorted(nums)
        op_arr = set()
        for i in range(len(arr)):
            x = arr[i]
            l = i+1
            r = len(arr)-1
            while(l<r):
                if(x+arr[l]+arr[r] > 0):
                    r-=1
                elif(x+arr[l]+arr[r] < 0):
                    l+=1
                else:
                    op_arr.add((x, arr[l], arr[r]))
                    l+=1
                    r-=1
        return(list(op_arr))
    except Exception as e:
        print(e)
        return