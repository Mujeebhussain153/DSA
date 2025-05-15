def findLargestThreeElements(arr):
    try:
        n = len(arr)
        if(n < 3):
            return None
        f = s = t = float('-inf')
        for i in range(n):
            if(arr[i] > f):
                t = s
                s = f
                f = arr[i]
            elif(arr[i] > s and arr[i]!=f):
                t = s
                s = arr[i]
            elif(arr[i] > t and arr[i]!=s and arr[i]!=f):
                t = arr[i]
        return f,s,t
    except Exception as e:
        print(e)
        return

print(findLargestThreeElements([99,7,8,9,12,14, 75]))