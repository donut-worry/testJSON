import json
from jsonGenerator import dataTypeGenerators as s
from faker import Faker
import random

fake = Faker()
depth = 6

stringGenerators = [s.get_text, s.get_paragraph, s.get_sentence, s.get_name, s.get_address]
numberGenerators = []


def getString():
    return random.choice(stringGenerators)()


def main():
    testStr = getString()
    print(testStr)


if __name__ == '__main__':
    main()
