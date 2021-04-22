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


def main():
    f = open("ingredientData.txt", "r")
    existing = set()
    # cont = input("Continue from previous?: ")
    cont = "Cheesy Pita Crisps"
    if cont != "":
        outfile = open("inglist", "r")
        for line in outfile:
            existing.add(line[:-1])
        outfile.close()
        line = f.readline()
        line = line.rstrip().split(";")
        while line[1] != cont:
            line = f.readline()
            line = line.rstrip().split(";")
        outfile = open("inglist", "a+")

    for line in f:
        line = line.rstrip()
        line = line.split(";")
        print(line[1])
        line = line[3:]
        for sub in line:
            if sub == "":
                break
            print(sub)
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
                    if ing not in existing:
                        existing.add(ing)
                        outfile.write(ing+";\n")


if __name__ == "__main__":
    main()
