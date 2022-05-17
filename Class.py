#PY類別學習

#定義類別與類別屬性(類別屬性是封裝在類別中的變數與函式)

from tkinter import Y


class IO :
    X_list = ["console","File"]
    def read(src):
        print("Read from",src)

print(IO.X_list)
IO.read("File")


#類別與實體物件,實體屬性
class CLASS_A:
    def __init__(self,x,y) -> None:
        self.x=x
        self.y=y
p1=CLASS_A(1,2)
p2=CLASS_A(3,4)
print(p1.x+p1.y,p2.x+p2.y)
