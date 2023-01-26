a =[10,34,12,14,54,41,15]


def sumA(a):
    i,j=0,len(a)-1
    l=[]
    m =[]
    r =[]
    l.append(a[i])
    suml=a[i]
    ans=0
    r.append(a[j])
    sumr=a[j]

    while i < j:


        if suml < sumr:
            i+=1
            suml += a[i]
            l.append(a[i])
            
        elif suml > sumr :
            j-=1
            sumr += a[j]
            r.append(a[j])
            
        
        elif suml == sumr :
            i+=1
            j-=1
            if abs(i)-abs(j)!=1:
                 m.append(a[i])
            ans = suml

    
    print(l , m , r,suml,sumr,ans) 
    if ans !=0:
        return ans
    else:
        return "not possible"

print(sumA(a))
        
