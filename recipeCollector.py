import requests
from bs4 import BeautifulSoup

recipeNames = {}
categoryURL = {}
URLS = ["https://recipes.fandom.com/wiki/Category:Appetizer_Recipes",
        "https://recipes.fandom.com/wiki/Category:Appetizer_Recipes?from=Stuffed+Eggs+Jalape%C3%B1o",
        "https://recipes.fandom.com/wiki/Category:Main_Dish_Recipes",
        "https://recipes.fandom.com/wiki/Category:Main_Dish_Recipes?from=Orange+Ham+Kabobs",
        "https://recipes.fandom.com/wiki/Category:Side_Dish_Recipes",
        "https://recipes.fandom.com/wiki/Category:Dessert_Recipes",
        "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Cherry+Rice+Cream",
        "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Fresh+Strawberry+Relish",
        "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Mocha+Dream+Bars",
        "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Spanish+Cheesecake",
        "https://recipes.fandom.com/wiki/Category:Beverage_Recipes"]

for url in URLS:
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find("ul", {"class": "category-page__members-for-char"})
    for ultag in soup.find_all("ul", {"class": "category-page__members-for-char"}):
        for litag in ultag.find_all('li', {"class": "category-page__member"}):
            name = litag.text.strip()
            link = litag.find('a')
            if name[:8] == "Category":
                categoryURL[name] = link['href']
            else:
                link = litag.find('a')
                recipeNames[name] = link['href']

for rec in recipeNames:
    print(rec, '->', recipeNames[rec])
for link in categoryURL:
    print(link, '->', categoryURL[link])
