from main_class import hangman


def main():
    word = hangman.main_game()
    hangman.player_play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = hangman.main_game()
        hangman.player_play(word)


if __name__ == "__main__":
    main()
