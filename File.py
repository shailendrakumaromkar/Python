import os

f=open("test.txt","a")
f.write("this is new line")
f.close()

f=open("test.txt","rt")
print(f.read())

print(f.readline())
print(f.readline())

for i in f:
    print(i)

f.close()

f=open("test4.txt","x")

if f:
    print("file created")

if os.path.exists("test2.txt"):
    os.remove("test2.txt")
else:
    print("file not exist")