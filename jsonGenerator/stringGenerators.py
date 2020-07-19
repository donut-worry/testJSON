from faker import Faker
import random

fake = Faker()
depth = 6


def getText(length=100):
    return fake.text(max_nb_chars=length)


def getParagraph(length=6):
    return fake.paragraph(nb_sentences=length, variable_nb_sentences=True)


def getName():
    return fake.name()


def getAddress():
    return fake.address()


def getSentence(length=16):
    return fake.sentence(nb_words=length, variable_nb_words=True)
