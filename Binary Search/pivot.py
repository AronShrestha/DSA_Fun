arr = [2,3,4,5,0,6,7,8,9]

def pivot(arr):
    left = 0
    right =len(arr)-1
    print(left-int((left-right)/2))

    mid = left-int((left-right)/2)
    while(left<right):
       
        print("mid {}".format(mid))
        if  arr[mid]>=arr[0]:
            print("mid")
            left = mid+1
        else:
            print(arr[0])
            print(arr[mid])
            print('r')
            right =mid

        mid = left-int((left-right)/2)
    return left

print(pivot(arr))