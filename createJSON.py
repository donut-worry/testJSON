import json
from random import randrange


depth = 16

myArr = ['foo', 'bar', 123]
myDict = {'foo': 123, 'bar': myArr}

# print("======== Array -> JSON ==========")
# print(json.dumps(myArr))
# print("======= Dictionary -> JSON =========")
# print(json.dumps(myDict))


def createObjects(cnt=depth):
    print("Will create {} objects".format(cnt))
    pass


def createArrays(deep=depth):
    print("Will create {} arrays".format(deep))
    pass


for x in range(depth):
    nObjects = randrange(depth)
    createObjects(nObjects)
    nArrays = randrange(depth)
    createArrays(nArrays)





