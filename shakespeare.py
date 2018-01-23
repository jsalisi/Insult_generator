import random

list_a = []
list_b = []
list_c = []


def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    print("Thou", word_a, word_b, word_c, '!')


with open("insults.csv", "r") as f:
    for line in f:
        lineArr = line.rstrip().split(',')
        list_a.append(lineArr[0])
        list_b.append(lineArr[1])
        list_c.append(lineArr[2])

insult_me()
