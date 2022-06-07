class Point:
    def __init__(self,x1,x2) -> None:
        self.m1 = x1
        self.m2 = x2
        pass

p = Point(1,5)
print(p.m1+p.m2)