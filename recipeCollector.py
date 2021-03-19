import requests
from bs4 import BeautifulSoup


def textOrganize():
    recipeNames = []
    categoryURL = {}
    categorylinks = open("categoryLink.txt", "w")
    # URLS = ["https://recipes.fandom.com/wiki/Category:Appetizer_Recipes",
    #         "https://recipes.fandom.com/wiki/Category:Appetizer_Recipes?from=Stuffed+Eggs+Jalape%C3%B1o",
    #         "https://recipes.fandom.com/wiki/Category:Main_Dish_Recipes",
    #         "https://recipes.fandom.com/wiki/Category:Main_Dish_Recipes?from=Orange+Ham+Kabobs",
    #         "https://recipes.fandom.com/wiki/Category:Side_Dish_Recipes",
    #         "https://recipes.fandom.com/wiki/Category:Dessert_Recipes",
    #         "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Cherry+Rice+Cream",
    #         "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Fresh+Strawberry+Relish",
    #         "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Mocha+Dream+Bars",
    #         "https://recipes.fandom.com/wiki/Category:Dessert_Recipes?from=Spanish+Cheesecake"]

    URLS = ["https://recipes.fandom.com/wiki/Category:Antipasto_Recipes",
            "https://recipes.fandom.com/wiki/Category:Bread_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Canap%C3%A9_Recipes",
            "https://recipes.fandom.com/wiki/Category:Cheese_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Chicken_wing_Recipes",
            "https://recipes.fandom.com/wiki/Category:Chilean_Appetizers",
            "https://recipes.fandom.com/wiki/Category:Dip_Recipes",
            "https://recipes.fandom.com/wiki/Category:Ethnic_and_Regional_Appetizers",
            "https://recipes.fandom.com/wiki/Category:Fondue_Recipes",
            "https://recipes.fandom.com/wiki/Category:Healthy_Appetizers",
            "https://recipes.fandom.com/wiki/Category:Meat_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Pastry_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Pizza_Recipes",
            "https://recipes.fandom.com/wiki/Category:P%C3%A2t%C3%A9_Recipes",
            "https://recipes.fandom.com/wiki/Category:Quick_and_Easy_Appetizers",
            "https://recipes.fandom.com/wiki/Category:Salsa_Recipes",
            "https://recipes.fandom.com/wiki/Category:Seafood_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Spread_Recipes",
            "https://recipes.fandom.com/wiki/Category:Stuffed_Biscuit_Recipes",
            "https://recipes.fandom.com/wiki/Category:Sweet_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Vegan_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Vegetarian_appetizer_Recipes",
            "https://recipes.fandom.com/wiki/Category:Budget_Friendly_Main_Dish_Recipes",
            "https://recipes.fandom.com/wiki/Category:Fondue_Recipes",
            "https://recipes.fandom.com/wiki/Category:Frittata_Recipes",
            "https://recipes.fandom.com/wiki/Category:Healthy_Main_Dishes",
            "https://recipes.fandom.com/wiki/Category:Main_Dish_Meat_Recipes",
            "https://recipes.fandom.com/wiki/Category:Main_Dish_Pasta_Recipes",
            "https://recipes.fandom.com/wiki/Category:Main_Dish_Poultry_Recipes",
            "https://recipes.fandom.com/wiki/Category:Main_Dish_Salad_Recipes",
            "https://recipes.fandom.com/wiki/Category:Main_Dish_Seafood_Recipes",
            "https://recipes.fandom.com/wiki/Category:Pizza_Recipes",
            "https://recipes.fandom.com/wiki/Category:Pot_pie_Recipes",
            "https://recipes.fandom.com/wiki/Category:Quiche_Recipes",
            "https://recipes.fandom.com/wiki/Category:Quick_and_Easy_Main_Dishes",
            "https://recipes.fandom.com/wiki/Category:Saudi_Arabian_Meat_Dishes",
            "https://recipes.fandom.com/wiki/Category:Vegan_Main_Dish_Recipes",
            "https://recipes.fandom.com/wiki/Category:Vegetarian_Main_Dish_Recipes",
            "https://recipes.fandom.com/wiki/Category:Baked_bean_Recipes",
            "https://recipes.fandom.com/wiki/Category:Breadstick_Recipes",
            "https://recipes.fandom.com/wiki/Category:Chutney_Recipes",
            "https://recipes.fandom.com/wiki/Category:Cornbread_Recipes",
            "https://recipes.fandom.com/wiki/Category:Cranberry_sauce_Recipes",
            "https://recipes.fandom.com/wiki/Category:Dumpling_Recipes",
            "https://recipes.fandom.com/wiki/Category:Garlic_bread_Recipes",
            "https://recipes.fandom.com/wiki/Category:Guacamole_Recipes",
            "https://recipes.fandom.com/wiki/Category:Kugel_Recipes",
            "https://recipes.fandom.com/wiki/Category:Pizza_Recipes",
            "https://recipes.fandom.com/wiki/Category:Pudding_Recipes",
            "https://recipes.fandom.com/wiki/Category:Quick_and_Easy_Side_Dishes",
            "https://recipes.fandom.com/wiki/Category:Relish_Recipes",
            "https://recipes.fandom.com/wiki/Category:Roll_Recipes",
            "https://recipes.fandom.com/wiki/Category:Salad_Recipes",
            "https://recipes.fandom.com/wiki/Category:Salsa_Recipes",
            "https://recipes.fandom.com/wiki/Category:Side_Dish_Fruit_Recipes",
            "https://recipes.fandom.com/wiki/Category:Side_Dish_Meat_Recipes",
            "https://recipes.fandom.com/wiki/Category:Side_Dish_Pasta_Recipes",
            "https://recipes.fandom.com/wiki/Category:Side_Dish_Poultry_Recipes",
            "https://recipes.fandom.com/wiki/Category:Side_Dish_Rice_Recipes",
            "https://recipes.fandom.com/wiki/Category:Side_Dish_Seafood_Recipes",
            "https://recipes.fandom.com/wiki/Category:Side_Dish_Vegetable_Recipes",
            "https://recipes.fandom.com/wiki/Category:Slaw_Recipes",
            "https://recipes.fandom.com/wiki/Category:Soup_Recipes",
            "https://recipes.fandom.com/wiki/Category:Stuffed_Biscuit_Recipes",
            "https://recipes.fandom.com/wiki/Category:Stuffing_Recipes",
            "https://recipes.fandom.com/wiki/Category:Vegan_Side_Dish_Recipes",
            "https://recipes.fandom.com/wiki/Category:Vegetarian_Side_Dish_Recipes",
            "https://recipes.fandom.com/wiki/Category:Atkins_Desserts",
            "https://recipes.fandom.com/wiki/Category:Cake_Recipes",
            "https://recipes.fandom.com/wiki/Category:Cheesecake_Recipes",
            "https://recipes.fandom.com/wiki/Category:Chilean_Desserts",
            "https://recipes.fandom.com/wiki/Category:Christmas_Desserts",
            "https://recipes.fandom.com/wiki/Category:Cobbler_Recipes",
            "https://recipes.fandom.com/wiki/Category:Crisp_Recipes",
            "https://recipes.fandom.com/wiki/Category:Custard_Recipes",
            "https://recipes.fandom.com/wiki/Category:Dessert_fondue_Recipes",
            "https://recipes.fandom.com/wiki/Category:Dessert_loaf_Recipes",
            "https://recipes.fandom.com/wiki/Category:Dessert_Salad_Recipes",
            "https://recipes.fandom.com/wiki/Category:Desserts_with_Rum",
            "https://recipes.fandom.com/wiki/Category:Ethnic_and_Regional_Desserts",
            "https://recipes.fandom.com/wiki/Category:Frozen_dessert_Recipes",
            "https://recipes.fandom.com/wiki/Category:Fruit_Desserts",
            "https://recipes.fandom.com/wiki/Category:Healthy_Desserts",
            "https://recipes.fandom.com/wiki/Category:Ice_cream_Recipes",
            "https://recipes.fandom.com/wiki/Category:Lindas_Busy_Kitchen_Desserts",
            "https://recipes.fandom.com/wiki/Category:Malawian_Desserts",
            "https://recipes.fandom.com/wiki/Category:No-bake_dessert_Recipes",
            "https://recipes.fandom.com/wiki/Category:Passover_Desserts",
            "https://recipes.fandom.com/wiki/Category:Pie_Recipes",
            "https://recipes.fandom.com/wiki/Category:Pudding_Recipes",
            "https://recipes.fandom.com/wiki/Category:Sherbet_Recipes",
            "https://recipes.fandom.com/wiki/Category:Strawberry_Desserts",
            "https://recipes.fandom.com/wiki/Category:Stuffed_Biscuit_Recipes",
            "https://recipes.fandom.com/wiki/Category:Torte_Recipes",
            "https://recipes.fandom.com/wiki/Category:Trifle_Recipes",
            "https://recipes.fandom.com/wiki/Category:Uruguayan_Appetizers",
            "https://recipes.fandom.com/wiki/Category:Valentine%27s_Day_Desserts",
            "https://recipes.fandom.com/wiki/Category:Vegan_dessert_Recipes",
            "https://recipes.fandom.com/wiki/Category:Vegetarian_Dessert_Recipes"]

    for url in URLS:
        print("CURRENT: " + url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find("ul", {"class": "category-page__members-for-char"})
        for ultag in soup.find_all("ul", {"class": "category-page__members-for-char"}):
            for litag in ultag.find_all('li', {"class": "category-page__member"}):
                name = litag.text.strip()
                link = litag.find('a')
                if name[:8] == "Category":
                    categorylinks.write('"' +
                                        "https://recipes.fandom.com" + link['href']+'",\n')
                elif not (name[:9] == "User blog"):
                    foodCategory = linkParse(url)
                    foodName = name
                    foodLink = "https://recipes.fandom.com" + link['href']
                    recipeNames.append([foodCategory, foodName, foodLink])

    file = open("foodLinks2.txt", "a+")
    # file.write("Type;Name;Link\n")
    for rec in recipeNames:
        file.write(rec[0]+";"+rec[1]+";"+rec[2]+"\n")


def linkParse(url):
    s = url.split(":")
    if "?" in s[2]:
        s = s[2].split("?")
        s = s[0]
    else:
        s = s[2]
    return s


def main():
    textOrganize()


if __name__ == "__main__":
    main()
