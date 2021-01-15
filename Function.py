"""
Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.



def func(fname,mname,lname):
    print("name " + fname)


func("raja")
func("kumar")
func("omkar")


func(mname="kumar",lname="omkar", fname="shailendra")


def func1(country="Bharat"):
    print("my country is: " + country )

func1()
func1("Gremany")


def func2(list2):
    for i in list2:
        print(i)

list1=["raja","kumar","omkar"]

func2(list1)

def func3(x):
    return x*5

#print(func3(4))

"""

def recurs(i):
    if (i>0):
        j=i+recurs(i-1)
        print(j)
    else:
        j=0
    return j


recurs(4)
