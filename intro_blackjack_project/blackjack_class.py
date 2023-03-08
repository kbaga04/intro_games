class values:
    @classmethod
    def findAceValue(cls, totalValue):
        if totalValue + 11 > 21:
            return 1
        else:
            return 11

    @classmethod
    def canContinue(cls, totalValue):
        if totalValue > 21:
            return False
        else:
            return True

    @classmethod
    def findWinner(cls, playerValue, player2Value, player2Name):
        if (player2Value == playerValue and player2Value <= 21) and playerValue <= 21:
            print("It's a TIE!")
            print("Want to try again")
        elif player2Value > playerValue and player2Value <= 21 and playerValue <= 21:
            print("Nice Job! ", player2Name, "Won")
            print("Want to Try Again?")
        elif (player2Value < playerValue and player2Value <= 21) and playerValue <= 21:
            print("Nice Job! Plyaer 1 Won!")
            print("Want to play again?")
