

def swap(a,r,c):
    a[r],a[c] = a[c],a[r]
    

def bubbleSort(a,r,c)->None:
    
    if r == 0:
        print("Sorting")
        return 
    elif r > c :
        if a[r]< a[c]:
            swap(a,r,c)
        bubbleSort(a,r,c+1)

    
    else:
        
        bubbleSort(a,r-1,0)


a=[1,5,3,2]
bubbleSort(a,3,0)
print(a)