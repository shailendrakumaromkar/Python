x= lambda y:y+10
print(x(4))

y=lambda a,b:a*b
print(y(3,4))

def lam(x):
    return lambda y:y*x

res=lam(2)
print(res(12))