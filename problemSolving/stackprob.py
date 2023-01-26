from queue import LifoQueue as stack

s1 = stack()
s2 = stack()
s3 = stack()
array =[]
for i in range(5,0,-1):
    s1.put(i)
array.append(s1)
array.append(s2)
array.append(s3)


size = array[0].qsize()

i = 0
item = None
while True:
    item = array[0].get()
    if array[1].empty():
        array[1].put(i)
    else:
        if past < item:
            


    past = item
    i += 1
