import random
from jsonGenerator import pyGenerators as g


def create_top_level_obj():
    return g.get_value()


def create_nested_obj(depth, result_dict=None):
    if result_dict is None:
        return create_nested_obj(depth, g.get_obj(10))
    if depth <= 0:
        return result_dict
    tmp_dict = g.get_obj()
    tmp_dict[random.choice(list(tmp_dict))] = create_nested_obj(depth-1, result_dict)
    result_dict[random.choice(list(result_dict))] = tmp_dict
    return result_dict


def create_nested_array(depth, result_list=None):
    if result_list is None:
        return create_nested_array(depth, g.get_array(10))
    if depth <= 0:
        return result_list
    tmp_list = g.get_array(10)
    tmp_list[random.randrange(0, len(tmp_list))] = create_nested_array(depth-1, result_list)
    result_list[random.randrange(0, len(result_list))] = tmp_list
    return result_list




#
# def createObjJson(cnt=depth):
#     print("Will create {} objects".format(cnt))
#     # cnt will be how deep this object is going to be
#     # cnt will default to global depth if not supplied
#     # this function should write out a JSON file at the end
#     pass
#
# def createArrJson(len=depth):
#     print("Will create {} arrays".format(len))
#     # len is going to be array length
#     # len will default to global depth if not supplied
#     # Call createArray function
#     # this function should write out Json file at the end
#     pass
#
# def createArray(len=depth):
#     print("Will create an array of length {} and return it".format(len))
#     # Create an array of a specific length and return it
#     # use fillArray() to fill each position in the array
#     pass
#
# def fillArray():
#     return myArr[randrange(len(myArr) - 1)]
#
# def createObj():
#     print("Will create an object ")
#     pass
#
#
# for x in range(depth):
#     nObjects = randrange(1, depth)
#     createObjJson(nObjects)
#     nArrays = randrange(1, depth)
#     createArrJson(nArrays)





