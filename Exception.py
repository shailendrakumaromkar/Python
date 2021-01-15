try:
    print(x)
except NameError:
    print("var not defined")
except:
    print("other error")
finally:
    print("this is finally block")

a=9
if a < 3:
    raise Exception("its incorrect")


# x = -1
# if x < 0:
#   raise Exception("Sorry, no numbers below zero")


d="raja"
if not type(d) is int:
    raise TypeError("data type mismatch")