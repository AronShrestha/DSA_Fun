st = "Ss went to ssschool"
 

def a(st):
    counter = 0
    le = len(st)
    flag = True
    
    while counter < le:
        if st[counter].lower() == "s":
            if st[counter+1].lower() == "s":
                flag = True
                while st[counter+1] == "s":
                    counter += 1
            else:
                return False
        counter +=1
    return flag
    


print(a(st))