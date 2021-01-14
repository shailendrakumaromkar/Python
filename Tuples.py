tup1=("raja","kumar","omkar","omkar")
print(tup1)

tup2=("one",)
print(tup2)

print(type(tup2))

tup3=tuple((1,2,3,4))
print(tup3)

print(tup3[0])
print(tup3[-1])
print(tup3[1:3])

x=list(tup1)
x[3]="shailendra"
tup1=tuple(x)
print(tup1)

(a,*b,c)=tup1
print(a)
print(b)
print(c)


for x in range(len(tup3)):
    print(tup3[x])

i=0
while i < len(tup3):
    print(tup3[i])
    i+=1

print(tup1*2)