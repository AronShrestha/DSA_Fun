import typing

def SumOfNumbers(n:int)->int:
    if n <= 0 :
        return 0
    else:
        rem = n %10
        next = int(n/10)
        return rem + SumOfNumbers(next)

print(SumOfNumbers(134))