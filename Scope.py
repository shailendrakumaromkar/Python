x=98

def one():
    global x
    x=3
    print(x)
    def two():
        print(x)
    two()

one()
print(x)
