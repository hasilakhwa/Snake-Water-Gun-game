import random
'''
Project 1: Snake, Water,Gun Game
We all have played snake, water gun game in our childhood If you haven't, google the rule
of this game and write a Python program capable of playing this game with the user

1 = snake
-1 = water
0 = gun
'''
computer = random.choice([1,-1,0])
you_str = input("Here: \n's' is for snake🐍 \n'w' is for Water🌊 \n'g' is for gun🔫 \nSo choose what's your input:")
you_dict = {"s": 1, "w":-1, "g":0}
you = you_dict[you_str]
reverse_dict = {1 : "Snake🐍", -1 : "Water🌊", 0 : "Gun🔫"} 

print(f"You choose: {reverse_dict[you]}\nComputer choose: {reverse_dict[computer]}")

if (computer == you):
    print("its a draw!🤝😐")
else:
    if(computer == 1 and you == -1):
        print("You Lose!😢💔")
    elif(computer == 1 and you == 0):
        print("You Win!🏆🎉")
    elif(computer == -1 and you == 1):
        print("You Win!🏆🎉")
    elif(computer == -1 and you == 0):
        print("You Lose!😢💔")
    elif(computer == 0 and you == 1):
        print("You Lose!😢💔")
    elif(computer == 0 and you == -1):
        print("You Win!🏆🎉")
    else:
        print("Un Expected case!The programmer of this game is noob😂🤣")            