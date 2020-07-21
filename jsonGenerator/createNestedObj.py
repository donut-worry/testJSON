import random
from jsonGenerator import pyGenerators as g
import simplejson as json


def create_top_level_obj(depth=None):
    return g.get_value()


def create_nested_obj(depth):
    result_dict = g.get_obj(15)
    result_dict[random.choice(list(result_dict))] = create_inner_nested_obj(depth - 1)
    return result_dict


def create_inner_nested_obj(depth):
    if depth <= 0:
        return
    tmp_dict = g.get_obj(21)
    tmp_random_key = random.choice(list(tmp_dict))
    tmp_dict[tmp_random_key] = create_inner_nested_obj(depth - 1)
    return tmp_dict


def create_nested_array(depth):
    result_list = g.get_array(25)
    result_list[random.randrange(0, len(result_list))] = create_inner_nested_array(depth - 1)
    return result_list


def create_inner_nested_array(depth):
    if depth <= 0:
        return
    tmp_list = g.get_array(10)
    tmp_random_pos = random.randrange(0, len(tmp_list))
    tmp_list[tmp_random_pos] = create_inner_nested_array(depth - 1)
    return tmp_list


def print_deep_dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            print_deep_dict(v)
        else:
            print(k, ":", v)


def main():
    # print(json.dumps(create_nested_obj(3),iterable_as_array=True))
    print(json.dumps(create_nested_obj(6)))
    # print_deep_dict(create_nested_obj(3))


if __name__ == '__main__':
    main()


