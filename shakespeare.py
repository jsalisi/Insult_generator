import random

from guizero import App, Text, Combo, PushButton

list_a = []
list_b = []
list_c = []


def insult_me():
    word_a = random.choice(list_a)
    word_b = random.choice(list_b)
    word_c = random.choice(list_c)
    return '{} {} {} {}{}'.format("Thou", word_a, word_b, word_c, '!')


def new_insult():
    message.set(insult_me())

def set_insult():
    message.set('{} {} {} {}{}'.format("Thou", menu1.value, menu2.value, menu3.value, '!'))


if __name__ == '__main__':
    with open("insults.csv", "r") as f:
        for line in f:
            lineArr = line.rstrip().split(',')
            list_a.append(lineArr[0])
            list_b.append(lineArr[1])
            list_c.append(lineArr[2])

    app = App(title="Shakespearean insult generator", width=450, height=300, layout="grid")

    message = Text(app, insult_me(), grid=[0, 0], align="left")
    rand_button = PushButton(app, new_insult, text="Insult me again", pady=5, padx=5, grid=[1, 0], align="left")

    menu1 = Combo(app, options=list_a, grid=[0, 2], align="top")
    menu2 = Combo(app, options=list_b, grid=[0, 3], align="top")
    menu3 = Combo(app, options=list_c, grid=[0, 4], align="top")

    use_button = PushButton(app, set_insult, text="Use insult", pady=5, padx=5, grid=[0, 5], align="top")

    app.display()
