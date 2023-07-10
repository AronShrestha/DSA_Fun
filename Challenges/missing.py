def solution(statues):
    statues.sort()
    n = len(statues)
    i=0
    temp = statues[0]
    needed = []
    while i < n:
        if (temp) == statues[i]:
            i = i+1
            temp+=1
        else:
            temp = temp+1
            needed.append(temp)
    return len(needed)

print(solution([2,5,8,9]))