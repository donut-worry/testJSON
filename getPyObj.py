import json
from jsonGenerator import stringGenerators as s
from faker import Faker
import random

fake = Faker()
depth = 6

stringGenerators = [s.getText, s.getParagraph, s.getSentence, s.getName, s.getAddress]
numberGenerators = []


def getString():
    return random.choice(stringGenerators)()


def main():
    testStr = getString()
    print(testStr)


if __name__ == '__main__':
    main()
