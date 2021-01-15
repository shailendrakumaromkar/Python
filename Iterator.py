name=["Raja","Kumar","Omkar"]
x=iter(name)

print(next(x))
print(next(x))
print(next(x))

fname="Raja"
f=iter(fname)

print(next(f))
print(next(f))
print(next(f))
print(next(f))

class Number:
    def __iter__(self):
        self.x=1
        return self
    
    def __next__(self):
        x=self.x
        self.x+=1
        return x

obj= Number()
res = iter(obj)

print(next(res))
print(next(res))
print(next(res))
print(next(res))

print(next(res))
print(next(res))
print(next(res))
print(next(res))