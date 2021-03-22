import requests
from bs4 import BeautifulSoup

f = open("foodLinks2.txt")
f.readline()

ingf = open("ingredientData.txt", "a+")


# type;name;link
for line in f:
    line = line.rstrip()
    line = line.split(";")
    print("INGRED: "+line[1])
    page = requests.get(line[2])
    ingredientList = line
    soup = BeautifulSoup(page.content, 'html.parser')
    ingredients = soup.find(lambda tag: tag.name ==
                            "h2" and "Ingredients" in tag.text)
    try:
        while ingredients.name != "ul":
            ingredients = ingredients.find_next_sibling()
        for litag in ingredients.find_all('li'):
            ingredientList.append(litag.text)
        for s in ingredientList:
            text = str(s) + ";"
            ingf.write(text)
        ingf.write("\n")
    except:
        pass


print("FINISHED")
