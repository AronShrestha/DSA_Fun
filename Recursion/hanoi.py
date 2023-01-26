



def TOH(n,Source,Helper,Destination):
    if n == 1:
        print(f"move a disk {n} from Source to Helper")
  
        temp = Source.pop()
        Destination.append(temp)
        print(f"{Source ,Helper,Destination}")

    else:
        TOH(n-1,Source,Destination,Helper)
        temp = Source.pop()
        Destination.append(temp)
       
        print(f"move a disk {n} from  Source to  Destination.")
        print(f"{Source ,Helper,Destination}")
        TOH(n-1,Helper,Source,Destination)
    

def TableOfHanoie(n,Source,Helper,Destination):
    if n == 1:
        print(f"move a disk {n} from {Source} to {Destination}.")
    else:
        TableOfHanoie(n-1,Source,Destination,Helper)
        print(f"move a disk {n} from {Source} to {Destination}.")
        TableOfHanoie(n-1,Helper,Source,Destination)




if __name__=='__main__':
    try:
        n = int(input("Enter the  number of disk in integer"))
    except ValueError:
        print(f"Sorry {n} is not a valid integer number for number of disk ")
    # TableOfHanoie(n,"Source","Helper","Destination")
    s1 = []
    s2 = []
    s3 = []

    for i in range(n,0,-1):
        s1.append((i))

    print(s1,s2,s3)
 
    TOH(n,s1,s2,s3)
    
            
    