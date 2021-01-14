a="raja"

def func():
    a="kumar"
    print(a)

func()
print(a)


def func1():
    global x
    x = "shailendra"
    print(x)

func1()
print(x)


y="neha"

def func2():
    global y
    y="kalbhor"
    print(y)

func2()
print(y)