import random
list=["snake","water","gun"]
i=0
b=random.choice(list)
while True:
    i=i+1
    if i>10:
        print("game over")
        break
    else:
        c = input("Please input s for snake ,w for water and g for gun :")
        if c == "s":
            a = list[0]
        elif c == "w":
            a = list[1]
        elif c == "g":
            a = list[2]
        else:
            print("Please inpur correct input ...")
        if c=="s" and b=="water":
            print("You win")
        elif c=="w" and b=="gun":
            print("You win")
        elif c=="g" and b=="snake":
            print("You win")
        elif c=="w" and b=="snake":
            print("computer win")
        elif c=="g" and b=="water":
            print("computer win")
        elif c=="s" and b=="gun":
            print("computer win")
        else:
            print("match get draw please input again")