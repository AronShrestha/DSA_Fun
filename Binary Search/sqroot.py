from re import S


number = 256

def sqrt(n):
    low=0
    high =n

    m = low - int((low-high)/2)
    ans=-1
    while low<=high:
        if m*m == n:
            return m
        elif m*m < n:
            ans = m
            low=m+1
        elif m*m>n:
            high = m-1
        m=low-int((low-high)/2)
    return ans

print(sqrt(number))