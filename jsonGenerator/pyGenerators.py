import simplejson as json
from jsonGenerator import dataTypeGenerators as gen
import random


stringGenerators = [gen.get_text, gen.get_paragraph, gen.get_sentence, gen.get_name, gen.get_address]
numberGenerators = [gen.get_int, gen.get_long, gen.get_float, gen.get_exp_number]
simpleObjGenerators = stringGenerators + numberGenerators + [gen.get_boolean, gen.get_null]
valueGenerators = [simpleObjGenerators, gen.get_list, gen.get_dict]


def get_string():
    return random.choice(stringGenerators)()


def get_number():
    return random.choice(numberGenerators)()


def get_value():
    return random.choice(valueGenerators)()


def get_array(length=20):
    my_list = []
    for _ in range(length):
        my_list.append(get_value())
    return my_list


def get_obj(length=10):
    my_obj = {}
    for _ in range(length):
        my_obj[gen.get_key()] = get_value()
    return my_obj


def main():
    #for _ in range(20):
        #print(get_string())
        #print(get_number())
        #print(get_value())
    print(json.dumps(get_obj()))
    #print(get_array())
    #print(json.dumps(gen.get_list()))

if __name__ == '__main__':
    main()
