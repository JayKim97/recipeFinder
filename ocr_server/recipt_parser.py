def new_ingredients(text, ingList):
    textArr = [line for line in text.split('\n') if line != ""]
    newIngs = []
    for text in textArr:
        for ing in ingList:
            if ing in text.lower():
                newIngs.append(ing)
    return newIngs


def pre_process():
    ingFile = open("./static/datas/inglist.txt", "r")
    return [ing.replace(";\n", "") for ing in ingFile]
    ingFile.close()


def userIng(newIngs):
    default = open('./static/datas/userDataDefault.txt', "r")
    user = open('./static/datas/userDataNew.txt', "w")
    for line in default:
        user.write(line)
    for ings in newIngs:
        user.write(ings+";\n")
    default.close()
    user.close()


text = """
27-PRODUCE
06038318654 PCO MUSH ENOKI = MR

4083 POTATO WHITE MR
0.425 kg @ $4. 39/kg
4166 ONIONS SWEET MR

0.485 kg @ $4. 39/kg
"""
ingList = pre_process()
newIngs = new_ingredients(text, ingList)
userIng(newIngs)
