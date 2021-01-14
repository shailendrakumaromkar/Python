print(4>3)
print(4<3)
print(4==3)

a=3
b=20

if (a>b):
    print("a is greater")
else:
    print("b is greater")

print(bool("raja"))
print(bool(23))


print(bool(False))
print(bool(None))
print(bool(0))
print(bool(()))
print(bool({}))
print(bool([]))
print(bool(""))

def test():
    return True

if test():
    print("True is return")
else:
    print("False is return")

a=23
print(isinstance(a,str))