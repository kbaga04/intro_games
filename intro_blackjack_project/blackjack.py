import random
from blackjack_class import values

playerValue = 0
player2Value = 0
dealerValue = 0
ace = values.findAceValue(playerValue)
king = 10
queen = 10
jack = 10
cardValues = [2, 3, 4, 5, 6, 7, 8, 9, 10, king, queen, jack, ace]

print("Great BlackJack Game!")

while (playerValue <= 21):
    ace = values.findAceValue(playerValue)
    randValue = cardValues[random.randint(1, len(cardValues) - 1)]
    playerValue += randValue
    print("The Value that you got is: ", randValue)
    print("Total Card Value: ", playerValue)
    if not values.canContinue(playerValue):
        print("Sorry, You Lost")
        print("Want to Try Again?")
        break
    print("Want to Continue? (y/n)")
    cont = input()
    if cont == "no" or cont == "n":
        print("Now, it is the Friend's or Computer's turn!")
        break
    else:
        continue

if playerValue <= 21:
    print("Want to play with a friend or a computer? (f/c)")
    userInput = input()
    if userInput == "friend" or userInput == "f":
        print("Ok, It is Player 2's turn")
        while (player2Value <= 21):
            ace = values.findAceValue(playerValue)
            randValue = cardValues[random.randint(1, len(cardValues) - 1)]
            player2Value += randValue
            print("The Value that you got is: ", randValue)
            print("Total Card Value: ", player2Value)
            if not values.canContinue(player2Value):
                print("Sorry, You Lost")
                print("Player 1 Won!")
                print("Want to Try Again?")
                break
            print("Want to Continue? (y/n)")
            cont = input()
            if cont == "no" or cont == "n":
                print("Ok, Let's Calculate Scores")
                break
            else:
                continue

if playerValue <= 21:
    if userInput == "friend" or userInput == "f":
        values.findWinner(playerValue, player2Value, "Player 2 ")
    if not (userInput == "friend" or userInput == "f"):
        print("Ok, It is the Computer's Turn")
        if playerValue <= 21:
            while (dealerValue <= 21):
                ace = values.findAceValue(playerValue)
                randValue = cardValues[random.randint(1, len(cardValues) - 1)]
                dealerValue += randValue
                print("The Dealer got: ", randValue)
                print("The Dealer's Total Value is: ", dealerValue)
                isContinue = random.randint(1, 10)
                if ((isContinue > 3 and dealerValue >= 18) or (isContinue > 7 and dealerValue >= 12)):
                    break
                if not values.canContinue(dealerValue):
                    print("You Won! The Dealer went over 21")
                    break
                else:
                    continue

    if not (userInput == "friend" or userInput == "f"):
        values.findWinner(playerValue, dealerValue, "Dealer ")
