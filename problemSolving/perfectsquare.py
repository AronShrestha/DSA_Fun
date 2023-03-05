def perfect_square(n:list):
    ans = []
    for num in range(1,n):
        print(num)
        a = num**(1/2)
        print(f"a {a}")
        if num**(1/2)%1 == 0:
            print(num)
            ans.append(num)
    
    return ans
    

print(perfect_square(100))
        