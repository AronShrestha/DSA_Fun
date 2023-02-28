class Batsman:

    def __init__(self, s1, s2):
        self.s1 = s1
        self.s2 = s2 
    
    def __add__(self, second):
        s1 = self.s1 + second.s1
        s2 = self.s2 + second.s2
        B3 = Batsman(s1, s2)

        return B3
    
    def __str__(self) -> str:
        return f"s1 {self.s1}  and s2 {self.s2}"



class Distance:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __sub__(self,second):
        x = self.x - second.x
        y = self.y -  second.y
        distance = Distance(x, y)
        return distance
    
    def __str__(self) -> str:
        return f"x {self.x} , y {self.y}"

# b1 = Batsman(1, 2)
# b2 = Batsman(3, 2)
# b3 = b1 + b2 
# # print(b3)
# d1 = Distance(10,30)
# d2 = Distance(4, 22)
# d3 = d1-d2
# print(d3)


class Player:
    def __init__(self, power) -> None:
        self.power = power
    
    def __sub__(self, opponent):
        return self.power - opponent.power
    
    def __gt__(self, opp):
        if self.power > opp.power :
            return "Your more powerful"
        else:
            return "Opponent more powerful"


class Enemy:
    def __init__(self, power) -> None:
        self.power = power


p1 = Player(100)
p2 = Enemy(20)
print(p1-p2)
print(p1>p2)
    
