# def string(s):
#     st = ""
#     for i in range(len(s)):
#         if s[i].lower() == "a":
#             continue
#         else:
#             st+=s[i]


#     return st


# print(string("My name is Aron Shrestha"))

def string(s,ans):
    """
    using recursion
    """
    if len(s)==0 :
        return ans
    else:
        if s[0].lower() != 'a':
            ans+=s[0]
        return string(s[1:],ans)

# a=""
# print(string("My name is Aron Shrestha",a))


def string2(s):
    """
    using recursion
    """
    if len(s)==0 :
        return ""
    else:
        ans =''
        if s[0].lower() != 'a':
            ans=s[0]
            return ans +string2(s[1:])
        else:
            return string2(s[1:])

# print(string2("Arona"))

def skipword(s):
    """
    Skip if sentence contains "word"
    """
    if len(s)==0 :
        return ""
    else:
        ans =''
        if s[0].lower() == 'w':
            temp = ""
            for i in range(4):
                temp+=s[i]
            if temp == "word":
                return skipword(s[4:])
        ans = s[0]
    return ans + skipword(s[1:])

# print(skipword("hello word i"))



def reversestring(s):
    if len(s)==0:
        return ""
    else:
        ans =''
        ans = s[0]
        return reversestring(s[1:])+ans

print(reversestring("Welcome to my channel"))


