

openning = "({["
closing = ")}]"

string = "(){}{{{}}}((()))({})"
def check_validity(string):
    stack = []
    for i in string:
        if i in openning:
            stack.append(i)
        
        else:
            if len(stack)<=0:
                return "invalid"
            
            else:
                check = stack.pop()
                if (check == "(" and i==")") or (check == "[" and i=="]") or (check=="{" and i =="}"):
                    continue
                else:
                    return "invalid"
        
    if len(stack)!= 0 :
        return "Invalid"
    else:
        return "valid"


print(check_validity(string))
