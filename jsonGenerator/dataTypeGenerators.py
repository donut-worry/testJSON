from faker import Faker
import random
import math
import datetime

fake = Faker()


def get_text(length=100):
    return fake.text(max_nb_chars=length)


def get_paragraph(length=6):
    return fake.paragraph(nb_sentences=length, variable_nb_sentences=True)


def get_name():
    return fake.name()


def get_address():
    return fake.address()


def get_sentence(length=16):
    return fake.sentence(nb_words=length, variable_nb_words=True)


def get_int():
    result = float(fake.random_int(min=-65535, max=65536))
    # print("get_int returns {}".format(type(result)))
    return result


def get_long():
    result = float(random.getrandbits(random.randrange(64, 256)))
    # print("get_long returns {}".format(type(result)))
    return result


def get_float():
    num = float(get_int())
    min_num = num / (num + (num / 10))
    max_num = num / (num + (num / 5))
    result = random.uniform(min_num, max_num)
    # print("get_float returns {}".format(type(result)))
    return result


def get_exp_number():
    # print("Exponential")
    multiplier = 1
    if (fake.boolean()):
        multiplier = -1
    if (fake.boolean()):
        num = random.randrange(40, 500)
    else:
        num = 1 / get_long()
    return math.expm1(num) * multiplier


def get_boolean():
    return fake.boolean()


def get_null():
    return None


def get_key():
    return fake.sentence() if fake.pybool() else fake.word()


def get_list():
    result = fake.pylist(nb_elements=50, variable_nb_elements=True)
    for i, s in enumerate(result):
        if isinstance(s, datetime.datetime):
            result[i] = s.isoformat()
    return result


def get_dict():
    result = fake.pydict(nb_elements=25, variable_nb_elements=True)
    for key, value in result.items():
        if isinstance(value, datetime.datetime):
            result[key] = value.isoformat()
    return result
