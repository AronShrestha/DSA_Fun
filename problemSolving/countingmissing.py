
def missing():
    n = int(input("Enter the number of elements you want"))
    ar = []
    maxn = -9999
    for i in range(n):
        num = int(input("Enter the element"))
        if maxn<num:
            maxn = num
        ar.append(num)
    count =0
    for num in range(maxn):
        if num not in ar:
            count+=1
            
        
    
    return count

print(missing())