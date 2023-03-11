

def recursive_palandrome(string):
    if len(string) == 0 or len(string) == 1:
        return True
    else:
        if (string[0] == string[len(string)-1]):
            return recursive_palandrome(string[1:len(string)-1])
    
    return False

print(recursive_palandrome(""))