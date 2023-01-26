a =[3,4,1,2,5,6,9,44,5,66,88,11]

def selectionSort(a:list):
    print("Given list {}".format(a))
    for i in range(len(a)-1):#last element will itself will be sorted
        min = i
        for j in range(i+1,len(a)):
            if a[min] > a[j]:
                min = j
        temp = a[i]
        a[i] = a [min]
        a[min]  = temp 
    print("List after selection sort {}".format(a))          



selectionSort(a)