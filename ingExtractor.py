def ingNameFinder(userIn, subArr):
    if userIn == "":
        return ""
    out = []
    if userIn[-1] == " ":
        userIn = userIn[:-1]
    if "," in userIn:
        userIn = userIn.split(",")
        for num in userIn:
            num = int(num)
            out.append(subArr[num])
    elif len(userIn) > 1:
        userIn = userIn.split(" ")
        temp = ""
        for num in userIn:
            num = int(num)
            temp = temp + subArr[num] + " "
        out.append(temp)

    else:
        userIn = int(userIn)
        out.append(subArr[userIn])
    return out


def addIngredient(sub, outfile):
    # sub = sub.replace("\xa0", " ")
    subArr = sub.split(" ")

    for i in range(len(subArr)):
        placeHolder = " "*len(subArr[i])
        print(i, end="")
        print(placeHolder, end="")
    print()
    userIn = input("toKeep: ")
    ingName = ingNameFinder(userIn, subArr)
    if ingName != "":
        for ing in ingName:
            if ing[-1] == " ":
                ing = ing[:-1]
            if ing[-1] == ",":
                ing = ing[:-1]
            outfile.write(ing.lower()+";\n")


def main():
    # recipes = open("ingredientData.txt", "r")
    recipes = open("newExamples.txt", "r")
    ingList = open("inglist.txt", "r")

    currentIng = []
    for line in ingList:
        currentIng.append(line.replace(";\n", ""))
    ingList.close()
    ingList = open("inglist.txt", "a+")
    counter = 0
    exist = False
    for line in recipes:
        line = line.rstrip().split(";")
        line = line[3:]
        for sen in line:
            sen = ''.join(
                [i for i in sen if (i.isalpha() or i == " ")]).lower()
            for ing in currentIng:
                if ing in sen:
                    exist = True
                    break
            if not exist and (sen != ""):
                print(sen)
                addIngredient(sen, ingList)
                counter += 1
            exist = False

    print(counter)
    # 1341


if __name__ == "__main__":
    main()

# sort -u -r inglist.txt > inglist2.txt && mv inglist2.txt inglist.txt
