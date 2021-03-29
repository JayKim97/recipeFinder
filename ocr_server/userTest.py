from random import randrange


def pre_process():
    ingFile = open("./static/datas/inglist.txt", "r")
    return [ing.replace(";\n", "") for ing in ingFile]


def randomSelect(num, ingList):
    for i in range(num):
        print(ingList[randrange(len(ingList))]+";")


randomSelect(50, pre_process())
