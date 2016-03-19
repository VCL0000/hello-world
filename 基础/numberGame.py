import random

number = random.randint(0,100)
guess = -1
print("游戏开始")
while guess != number:
    guess = int(input("input,0-100..."))

    if guess == number:
        print("good")
    elif guess < number:
        print("小了")
    elif guess > number:
        print("大了")
