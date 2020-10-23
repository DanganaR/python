import random
player1score = 0
player2score = 0
Green = 5
while Green < 10:
    rps = ['Rock', 'Paper', 'Scissors']
    player1 = random.choice(rps)
    print(player1)
    player2 = (input("enter rock, paper or scissors"))
    if player1score >= 3:
        print("Player 1 Wins!")
        Green = 11
    if player2score >= 3:
        print("Player 2 Wins!")
        Green = 11
    if player1 == player2:
        print("tie")
    elif ((player1 == "Paper" and player2 == "Rock") or (player1 == "Scissors" and player2 == "Paper") or
          (player1 == "Rock" and player2 == "Scissors") or (player2 == "Rock" and player1 == "Paper") or
          (player2 == "Paper" and player1 == "Scissors") or (player2 == "Scissors" and player1 == "Rock")):
        player1score = player1score + 1
        print("player1:", player1score, "player2:", player2score)
    elif (player2 == "Paper" and player1 == "Rock") or (player2 == "Scissors" and player1 == "Paper") \
            or (player2 == "Rock" and player1 == "Scissors"):
        player2score = player2score + 1
        print("player1:", player1score, "player2", player2score)

