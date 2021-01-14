str = "Raja Kumar"

print(str)
print(str[0])
print(str[4])
print(str[3:6])
print(str[2:])
print (str*3)
print(str + " Omkar")
print()

a="""hello my name is raja
how r u
good morning
"""
print(a)

print()

b="rajam omkar"
print(b[4])
print(len(b))

print()

for c in "Shailendra":
    print(c)
#    print(len(c))
print(len(c))


text="Mera naam hai"
print("Mera" not in text)

if "naam" not in text:
    print("name is present")


print(text[2:6])
print(text[2:])
print(text[:6])


b = "Hello, World!"
print(b[-8:-3])

a="raja Kumar"
print(a.upper())

a="KLDJKLD"
print(a.lower())

a="  kfjklsfsdf  "
print(a.strip())


a="Raja Kumar"
print(a.replace("a","z"))

a="Raja, Omkar"
print(a.split(","))

a="raja"
b="omkar"
print(a+" "+b)

a="My name is Raja & I am {2} years old, My weight is {1}. Call me @{0}"
b=34
c=66
d=9874563210
print(a.format(d,c,b))

a="Raja is \"gr\'8\" & he is \\awesome & \tpowerfull"
print(a)

