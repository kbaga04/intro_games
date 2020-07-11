import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        Tictactoe game = new Tictactoe();
        String player = "X";

        do {
            System.out.println(game.printBoard());
            System.out.println("enter row for " + player + " (0-2) or -1 to exit: ");
            int row = input.nextInt();
            if (row == -1)
                break;
            System.out.println("enter column for " + player + " (0-2) : ");
            int column = input.nextInt();
            game.setGame(row, column, player);
            if (game.isGameOver()) {
                System.out.println(game.printBoard() + "\n" + player + " wins!");
                break;
            }
            if (player == "X") {
                player = "O";
            } else {
                player = "X";
            }
        } while (true);
        System.out.println("Nice Game!..");

    }

}