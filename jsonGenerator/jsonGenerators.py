import json
from jsonGenerator import dataTypeGenerators as gen
import random

depth = 6

stringGenerators = [gen.get_text, gen.get_paragraph, gen.get_sentence, gen.get_name, gen.get_address]
numberGenerators = [gen.get_int, gen.get_long, gen.get_float, gen.get_exp_number]


def getString():
    return random.choice(stringGenerators)()

def getNumber():
    return random.choice(numberGenerators)()


def main():
    for _ in range(20):
        print(getString())
        print(getNumber())


if __name__ == '__main__':
    main()