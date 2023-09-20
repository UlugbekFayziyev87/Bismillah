player1 = int(input("Выбери число игрок 1, 1- Ножницы, 2- Камень, 3- Бумага"))
print (player1)
if player1 == 1:
    print("Ножницы")
elif player1 == 2:
    print("Камень")
elif player1 == 3:
    print("Бумага")
else:
    print("не верное число")
player2 = int(input("Выбери число игрок 2, 1- Ножницы, 2- Камень, 3- Бумага"))
print (player2)
if player2 == 1:
    print("Ножницы")
elif player2 == 2:
    print("Камень")
elif player2 == 3:
    print("Бумага")
else:
    print("не верное число")
if player1 == player2:
    print("Ничья")
elif player1 == 1 and player2 == 2 or player1 == 3 and player2 == 1:
    print("Победа player2")
elif player1 == 1 and player2 == 3 or player1 == 3 and player2 == 2:
    print("Победа player1")
