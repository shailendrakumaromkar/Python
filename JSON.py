import json

x='{"name":"raja","age":30,"city":"betul"}'

y=json.loads(x)
print(y["name"])

a={
    "car":"fortuner",
    "bike":"bullet",
    "phone":"iphone"
}

b=json.dumps(a)

print(b)

print(json.dumps(["a",1,2,3,True,False,None]))

d={
    "name":"neha",
    "age":30,
    "married":True,
    "hobbies":{
        "cooking":"Yes",
        "Gardening":"Yes"
    }
}

print(json.dumps(d,indent=10, separators=("$","#"),sort_keys=True))