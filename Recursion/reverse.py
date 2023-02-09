# def rev(n,i):
#     if (n%10==n):
#         return n
#     else:
#         temp =1
#         for k in range(i):
#             temp*=10
#         i-=1
#         rem =n%10
#         return rem*temp+rev(int(n/10),i)

# print(rev(58963,4))
import typing 

def rev(n:int)->int:
    if (n%10==n):
        return n
    else:
        