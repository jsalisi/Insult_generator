import random

from guizero import App, Text, PushButton, Combo

list_a = []
list_b = []
list_c = []

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

    app = App(title = "Shakespearean insult generator", layout = "grid")

    thou = Text(app, "Thou", grid=[1,0], align="left")

    insults_menu(app, [list_a, list_b, list_c])

    exclamation = Text(app, "!", grid=[5,0], align="left")

    app.display()
