# Function to calculate Maximum sub array sum when fixed length of subarray is explicitly provided
def maximumSubarraySum(arr, k):
    try:
        n = len(arr)
        if(n<=k):
            return -1
        window_sum = sum(arr[0:k])
        max_sum = window_sum
        for i in range(k, n):
            window_sum = window_sum - arr[i-k]+arr[i]
            max_sum = window_sum if window_sum > max_sum else max_sum
        return max_sum
    except Exception as e:
        print(e)
        return

print(maximumSubarraySum([1, 4, 2, 10, 2, 3, 1, 0, 20], 3))