import os
import random
from math import pi
os.system("cls")

baldur_online = True

if baldur_online:
    while True:
        try:
            height = float(input("You're height in m: "))
            break
        except:
            print("Write your height in numbers and a . if you have a decimal")
            continue

    if height >= 1.2 and height <= 1.99:
        print("You can go on baldur(=")
    else:
        if height < 1.2:
            print("You're too short")
        else:
            print("You're too tall")
else:
    print("Baldur is offline")

name = str(input("What's your name: "))
while True:
    try:
        age = int(input("How old are you: "))
        break
    except:
        print("Only use integers")
        continue

while True:
    try:
        weight = float(input(f"Welcome {name}! \nHow much do you weight: "))
        break
    except:
        print("Only use numbers ")
        continue
print("Your BMI is around", weight//height**2)

radius = float(input("How long is your circles radius: "))
circle_area = radius ** 2 * pi
print(f"your circles area is {circle_area:.3F} units^2")

rolls_completed = 0
number_list = []
while True:
    try:
        random_times = int(input("How many numbers to you want to randomize: "))
        break
    except:
        print("plz only real numbers")
        continue
while rolls_completed < random_times:
    die = random.randint(1,6)
    print(die)
    rolls_completed += 1

"""
# my way to randomize dice throws

number_list = []
while True:
    try:
        random_times = int(input("How many numbers to you want to randomize: "))
        break
    except:
        print("plz only real numbers")
        continue
for i in range(random_times):
    random_number = random.randint(1,6)
    number_list.append(random_number)
print(number_list)
print(f"The avrage value of the random numbers are: {sum(number_list) / len(number_list)}")
"""