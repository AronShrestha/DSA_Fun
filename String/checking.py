
def sfinder(st):
    flag = True
    maxl = len(st)
    count = 0
    while count < maxl: 
    
        if st[count].lower() =="s":
            count+=1
            if st[count].lower() != "s":
                return False
            else:
                
                while st[count].lower() =="s":
                    count+=1
        else:
            count+=1
    return flag

print(sfinder("sShe went to  sssssssssschool"))