set1={"raja","kumar","omkar","kumar"}
print(set1)
print(len(set1))

for x in set1:
    print(x)

set1.add("shailendra")
print(set1)

set2={1,2,3,4}
set1.update(set2)
print(set1)


set1.remove(4)
print(set1)

#set1.remove(5)
print(set1)

set1.discard(3)
print(set1)

y=set1.pop()
print(y)
print(set1)

set2={"raja","kumar"}
#set1.intersection_update(set2)
set1.intersection(set2)
print(set1)


set1.symmetric_difference_update(set2)
print(set1)