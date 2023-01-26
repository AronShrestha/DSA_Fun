# def Hello():
#     Hello1()
#     print(1)

# def Hello1():
#     Hello2()
#     print(2)

# def Hello2():
#     print(3)



# Hello()



def fibo(n):
    if n ==0 or n == 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(30))