import random
#1-stone
#2-clips
#3-paper
player= int(input("сделайте свой выбор"))
computer= random.randint(1,3)
if player== 1:
    print("вы выбрали камень")
elif player == 2:
    print("вы выбрали ножницы")
else:
    print("вы выбрали бумагу")

if computer== 1:
    print("компьютер выбрал камень")
elif computer == 2:
    print("компьютер выбрал ножницы")
else:
    print("компьютер выбрал бумагу")

if player == computer:
    print("ничья")
elif (player== 1 and computer==2) or (player== 2 and computer==3) or (player== 3 and computer== 1):
    print("игрок победил")
else:
    print("компьютер победил")


