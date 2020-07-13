import json
from random import randrange


depth = 16

myArr = ['foo', 'bar', 123]
myDict = {'foo': 123, 'bar': myArr}

# print("======== Array -> JSON ==========")
# print(json.dumps(myArr))
# print("======= Dictionary -> JSON =========")
# print(json.dumps(myDict))

def createObjJson(cnt=depth):
    print("Will create {} objects".format(cnt))
    # cnt will be how deep this object is going to be
    # cnt will default to global depth if not supplied
    # this function should write out a JSON file at the end
    pass

def createArrJson(len=depth):
    print("Will create {} arrays".format(len))
    # len is going to be array length
    # len will default to global depth if not supplied
    # Call createArray function
    # this function should write out Json file at the end
    pass

def createArray(len=depth):
    print("Will create an array of length {} and return it".format(len))
    # Create an array of a specific length and return it
    # use fillArray() to fill each position in the array
    pass

def fillArray():
    return myArr[randrange(len(myArr) - 1)]

def createObj():
    print("Will create an object ")
    pass


for x in range(depth):
    nObjects = randrange(depth)
    createObjJson(nObjects)
    nArrays = randrange(depth)
    createArrJson(nArrays)





