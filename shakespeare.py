# import random

from guizero import App, Text, Combo  # , PushButton

list_a = []
list_b = []
list_c = []

'''
def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    return '{} {} {} {} {}'.format("Thou", word_a, word_b, word_c, '!')


def new_insult():
    message.set(insult_me())
'''

def insults_menu(app_name, insult_list):
    position = 2
    for insults in insult_list:
        Combo(app_name, options=insults, grid=[position, 0], align="left")
        position += 1

if __name__ == '__main__':
    with open("insults.csv", "r") as f:
        for line in f:
            lineArr = line.rstrip().split(',')
            list_a.append(lineArr[0])
            list_b.append(lineArr[1])
            list_c.append(lineArr[2])

    app = App(title="Shakespearean insult generator", layout="grid")

    thou = Text(app, "Thou", grid=[1, 0], align="left")

    insults_menu(app, [list_a, list_b, list_c])

    exclamation = Text(app, "!", grid=[5, 0], align="left")

    # message = Text(app, insult_me())
    # button = PushButton(app, new_insult, text="Insult me again")

    app.display()
