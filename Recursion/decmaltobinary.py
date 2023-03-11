

def dectobi(num):
    if num <= 1:
        return str(num)
    else:
        if num%2 == 0 :
            return dectobi(num//2) + "0"
        else:
            return dectobi(num//2) + "1"


print(dectobi(40))
