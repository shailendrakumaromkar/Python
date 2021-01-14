dict1={
    "first":"Raja",
    "middle":"Kumar",
    "last":"Omkar",
    "first":"shailendra"
}

print(dict1)

print(dict1["last"])
print(len(dict1))
print(dict1.get("last"))
print(dict1.keys())
dict1["gender"]="Male"
print(dict1.keys())
print(dict1.values())
dict1["first"]="Raja"
print(dict1.values())
print(dict1.items())

if "middle" in dict1:
    print("middle name xist")

dict1.update({"first":"Neha"})
print(dict1)

dict1.pop("gender")
print(dict1)

dict1.popitem()
print(dict1)

for i in dict1:
    print(i)

for i in dict1:
    print(dict1[i])

for i in dict1.values():
    print(i)

for i in dict1.keys():
    print(i)

for x,y in dict1.items():
    print(x,y)

dict2=dict1.copy()
print(dict2)

dict3=dict(dict1)
print(dict3)