from faker import Faker
import random
import math

fake = Faker()


# depth = 6


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
    #print("Int")
    return fake.random_int(min=-65535, max=65536)


def get_long():
    #print("Long")
    return random.getrandbits(random.randrange(64, 256))


def get_float():
    #print("Float")
    num = float(get_int())
    min_num = num / (num + (num/10))
    max_num = num / (num + (num/5))
    return random.uniform(min_num, max_num)


def get_exp_number():
    #print("Exponential")
    multiplier = 1
    if(fake.boolean()):
        multiplier = -1
    if(fake.boolean()):
        num = random.randrange(40, 500)
    else:
        num = 1/get_long()
    return math.expm1(num) * multiplier
