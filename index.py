import os
os.system("cls")

#Villkor med ifsats:

""" villkor är i stort sett att kontrollera utfall
age = int(input("How old are you? \n"))
if age >= 18:
    print("you can go to the pub")
elif age < 15:
    print("your less than 15")
else:
    print("You're too young - get good!")   #indenteringar är viktiga
"""

"""
#My Version

baldur_online = True
height = float(input("Your height in m: "))

if baldur_online == True and height >= 1.2 and height <= 1.99:
    print("you can go")
elif baldur_online == False:
    print("baldur_online is offline")
elif height < 1.2:
    print("You're to short")
elif height > 1.99:
    print("You're to tall")
else:
    print("idk wtf is wrong")
"""

"""
#Better version

baldur_online = False

if baldur_online:
    height = float(input("You're height in m: "))
    if height >= 1.2 and height <= 1.99:
        print("You can go")
    else:
        print("You're alowed")
else:
    print("Baldur is offline")
"""