def solution(sequence):
    count =0
    n = len(sequence)-1
    i = 0
    high = -1
    
    while i<n:
        if high < sequence[i]:
            high = sequence[i]
        if count > 1:
            return False
        if sequence[i]>sequence[i+1] :
            count+=1

        i+=1
    if count >1:
        return False
    return True
        
        
        

        
        
print(solution([1,3,3,1,6,1]))
