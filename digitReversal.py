def digitReversal(digit):
    try:
        val=0
        n = digit
        while(n!=0):
            mod = n%10
            val = val*10+mod
            n//=10
        return val
    except Exception as e:
        print(e)
        return
    
print(digitReversal(12))