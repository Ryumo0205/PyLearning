#PY類別學習

#定義類別與類別屬性(類別屬性是封裝在類別中的變數與函式)

class IO :
    X_list = ["console","File"]
    def read(src):
        print("Read from",src)

print(IO.X_list)
IO.read("File")


#類別與實體物件,實體屬性
