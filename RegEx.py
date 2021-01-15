import re

str="My name is raja"
srch = re.search("^My .*ja$",str)

if srch:
    print("M found")
else:
    print("not found")


res=re.findall("a",str)
print(res)

sp=re.split("a",str)
print(sp)

sp=re.split("a",str,1)
print(sp)

sp=re.split("a",str,2)
print(sp)

sp=re.sub("\s", "*",str)
print(sp)