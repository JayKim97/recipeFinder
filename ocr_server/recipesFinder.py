class Recipe:
    def __init__(self, name, link, ings):
        self.name = name
        self.link = link
        self.ings = ings


def pre_process():
    recipeDataBase = open("./static/datas/ingredientData.txt", "r")
    recipes = []
    for line in recipeDataBase:
        line = line.split(';')
        name = line[1]
        link = line[2]
        temp = [ing for ing in line[3:] if ing != "" and ing != "\n"]
        ings = {}
        for ele in temp:
            ings[ele] = False
        recipes.append(Recipe(name, link, ings))
    recipeDataBase.close()
    return recipes


def recipeCheck(recipe, userIngs):
    for recIng in recipe.ings:
        for userIng in userIngs:
            if userIng in recIng:
                recipe.ings[recIng] = True
                break
    for recIng in recipe.ings:
        if not recipe.ings[recIng]:
            return
    print(recipe.name + " LINK: "+recipe.link)


def thisIsForTest():
    user = open('./static/datas/userDataNew.txt', "r")
    userIngs = [ing.replace(";\n", "") for ing in user]
    user.close()
    return userIngs


recipes = pre_process()
userIngs = thisIsForTest()
for recipe in recipes:
    recipeCheck(recipe, userIngs)
