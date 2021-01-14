list2=[1,2.4,"raja","raja","kumar","kumar","shailendra","neha"]
list1 = [1,"omkar"]
list1[0]="Shailendra"
list1[1]="New Omkar"
list3=["mera","bharat","mahan"]
print(list2)
print(list2[2])
print(list2[1:4])
print(list2[2:])
print(list2*2)
print(list2+list1)
print(len(list2))
print(type(list2))

x=list(("hamari","family","hogi","very","happy","waali"))
print(x)
print(x[-2])
print(x[2:5])
print(x[:5])
print(x[-6:-2])

print(x)
x[0]="complete"
print(x)
x[1:2]="full","omkar"
print(x)
x.insert(0,"betul")
print(x)
x.append("MP")
print(x)

x.append(list2)
print(x)

list2.append(list3)
print(list2)

list2.remove(2.4)
print(list2)

list2.pop(0)
print(list2)
list2.pop()
print(list2)

del list2[1]
print(list2)

for i in list2:
    print(i)

for j in range(len(list2)):
    print(j, list2[j])
    print(list2[j])

k=0
while k < len(list2):
    print(list2[k])
    k+=1

for l in list2:
    print(l)

list4=[]

list4.append(list2)
print(list2)
print(list4)

list5=[]
for i in list2:
    if "n" in i:
        list5.append(i)
        print(list5)


print(list2)
list2.sort(reverse=True)
print(list2)


def funcSort(n):
    return abs(n-50)

list6=[40,50,60,30,70]

list6.sort(key=funcSort)
print(list6)

list2.reverse()
print(list2)


list11=["a","b","c","d"]
list12=list11.copy()
print(list12)

list12=list(list11)
print(list12)

list13=[1,2,3,4]

for i in list11:
    list13.append(i)
print (list13)